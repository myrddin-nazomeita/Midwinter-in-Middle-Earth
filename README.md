# Midwinter-in-Middle-Earth
---
## Overview
"Midwinter in Middle-Earth" is a web application designed for managing gift lists during the Christmas/other season. It allows users to enter gifts they desire, view others' lists, and mark gifts as purchased, all while maintaining the surprise element by not revealing who bought the gift.

## Key Features

### User Authentication
- **Username/Password Authentication**: Users can log in using their credentials. The user data is managed using JSON for simplicity.
- **Session Management**: User sessions are handled to keep track of the logged-in user.

### Gift List Management
- **Personal Gift List**: Users can view and add new items to their own list, specifying a title, link, and comment for each gift.
- **Viewing Others' Lists**: Users can view gift lists of other users but not the full list of they own.
- **Gift Purchase Functionality**: Users can mark items on others' lists as purchased to avoid duplicate gifts.
- **Anonymity in Gifting**: When a user marks a gift as purchased, it's recorded, but the buyer's identity is not revealed to the gift recipient.
- **Remove Gifts**: User can remove gifts from lists.

## Technical Stack
- **Flask (Python)**: Backend is developed using the Flask framework, providing a lightweight and flexible platform.
- **JSON for Data Storage**: User data and gift lists are stored in JSON files (`users.json` and `gift_lists.json`), allowing for straightforward data management.
- **HTML/CSS for Frontend**: The `index.html` file, along with associated CSS, provides the user interface for the application.

## Installation and Setup
- **Docker Support**: The application is Docker-ready, ensuring easy setup and deployment.
- **Python Dependencies**: Dependencies are managed through a `requirements.txt` file.

## Codebase Overview

### `app.py`
- **Main Application Logic**: Handles routing, user authentication, session management, and interaction with JSON data files.
- **Endpoints**: Includes endpoints like for login, logout, viewing the gift list, and adding new gifts etc.

### `index.html`
- **User Interface**: The main page of the application, allowing users to add gifts, view their list, and see others' lists.
- **Dynamic Content Rendering**: Uses Jinja2 templating for dynamically displaying gift lists and user-specific information.
  
...

---
