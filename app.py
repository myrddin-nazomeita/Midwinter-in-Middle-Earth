from flask import Flask, render_template, request, redirect, session, url_for
import json

app = Flask(__name__)
app.secret_key = 'your_secret_key'

# Load Users
def load_users():
    with open('data/users.json') as f:
        return json.load(f)

# Load Gift Lists
def load_gift_lists():
    with open('data/gift_lists.json') as f:
        return json.load(f)

# Save Gift Lists
def save_gift_lists(gift_lists):
    with open('data/gift_lists.json', 'w') as f:
        json.dump(gift_lists, f, indent=4)

@app.route('/')
def index():
    if 'username' in session:
        gift_lists = load_gift_lists()
        return render_template('index.html', username=session['username'], gift_lists=gift_lists, enumerate=enumerate)
    return redirect(url_for('login'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        users = load_users()
        username = request.form['username']
        password = request.form['password']
        if username in users and users[username] == password:
            session['username'] = username
            return redirect(url_for('index'))
        else:
            return 'Login Failed'
    return render_template('login.html')

@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('login'))

@app.route('/add', methods=['POST'])
def add_gift():
    if 'username' in session:
        gift_lists = load_gift_lists()
        list_owner = request.form['list_owner']
        user_list = gift_lists.get(list_owner, [])
        user_list.append({
            'title': request.form['title'],
            'link': request.form['link'],
            'comment': request.form['comment'],
            'purchased': False,
            'added_by': session['username']
        })
        gift_lists[list_owner] = user_list
        save_gift_lists(gift_lists)
    return redirect(url_for('index'))

@app.route('/purchase/<username>/<gift_index>')
def purchase_gift(username, gift_index):
    if 'username' in session and session['username'] != username:
        gift_lists = load_gift_lists()
        if username in gift_lists and len(gift_lists[username]) > int(gift_index):
            gift_lists[username][int(gift_index)]['purchased'] = True
            save_gift_lists(gift_lists)
    return redirect(url_for('index'))

@app.route('/unpurchase/<username>/<gift_index>')
def unpurchase_gift(username, gift_index):
    if 'username' in session and session['username'] != username:
        gift_lists = load_gift_lists()
        if username in gift_lists and len(gift_lists[username]) > int(gift_index):
            gift_lists[username][int(gift_index)]['purchased'] = False
            save_gift_lists(gift_lists)
    return redirect(url_for('index'))

@app.route('/remove/<string:user>/<int:index>')
def remove_gift(user, index):
    # Ensure that the user is logged in
    if 'username' in session:
        try:
            # Load the current gift lists from the JSON file
            with open('data/gift_lists.json', 'r') as file:
                gift_lists = json.load(file)

            # Debugging print
            print(f"Gift lists loaded: {gift_lists}")

            # Ensure the user and index are valid before attempting to remove the gift
            if user in gift_lists and index < len(gift_lists[user]):
                # Remove the gift at the specified index
                del gift_lists[user][index]

                # Debugging print
                print(f"Gift at index {index} removed.")

                # Save the updated gift lists back to the JSON file
                with open('data/gift_lists.json', 'w') as file:
                    json.dump(gift_lists, file, indent=4)
        except Exception as e:
            # Debugging print
            print(f"An error occurred: {e}")
# Redirect to the index page or the appropriate page for the gift list
    return redirect(url_for('index'))


if __name__ == '__main__':
    app.run(debug=False)
