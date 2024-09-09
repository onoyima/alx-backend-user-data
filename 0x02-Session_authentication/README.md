# clinton boniface code 
# Session Authentication Project - README
Table of Contents
Project Overview
Requirements
Project Setup
Tasks Overview
Task 0: Et moi et moi et moi!
Task 1: Empty Session
Task 2: Create a Session
Task 3: User ID for Session ID
Testing
License
Project Overview
This project focuses on implementing a session-based authentication mechanism for a Python-based REST API, built on top of previous work using basic authentication. The project introduces the concept of session management, allowing users to authenticate and retrieve data based on active session IDs. It builds incrementally through a series of tasks that expand upon user access management via session authentication.

Requirements
All Python files are interpreted/compiled on Ubuntu 18.04 LTS using Python 3.7.
All files should end with a new line.
The first line of each file must be exactly: #!/usr/bin/env python3.
A README.md file, located at the root of the project folder, is mandatory.
Code must follow the pycodestyle guidelines (version 2.5).
All files must be executable.
File length will be tested using wc.
All modules, classes, and functions should include documentation that explains their purpose (this will be validated for completeness).
Documentation Requirements:
Modules: Each module should have a descriptive docstring explaining its purpose.
Classes: Every class should have a docstring explaining its function.
Functions: All functions, both inside and outside classes, should have a detailed docstring.
Project Setup
Clone the repository:

bash
Copy code
git clone https://github.com/your_username/alx-backend-user-data.git
Navigate to the project directory:

bash
Copy code
cd 0x02-Session_authentication
Ensure all dependencies are installed and use Python 3.7 for execution.

Run the application by starting the Flask server:

bash
Copy code
API_HOST=0.0.0.0 API_PORT=5000 AUTH_TYPE=session_auth python3 -m api.v1.app
Tasks Overview
Task 0: Et moi et moi et moi!
Objective: Extend the basic authentication implemented in the previous project by adding a new endpoint /users/me. This endpoint retrieves the authenticated user object if the authentication is successful.

Key Steps:
Copy the models and api folders from the previous Basic Authentication project.
Implement the new endpoint /api/v1/users/me to return the authenticated user details.
Update @app.before_request in api/v1/app.py to assign the result of auth.current_user(request) to request.current_user.
Modify the route in api/v1/views/users.py to handle requests where <user_id> is "me".
Usage:

bash
Copy code
# Create a new user and get authentication details
$ python3 main_0.py

# Retrieve user data using the "me" endpoint with the correct credentials
$ curl -H "Authorization: Basic <Base64_Credentials>" http://0.0.0.0:5000/api/v1/users/me
Task 1: Empty Session
Objective: Create an empty SessionAuth class that inherits from the Auth class, preparing for session-based authentication.

Key Steps:
Create the SessionAuth class in api/v1/auth/session_auth.py.
Ensure the SessionAuth class can be switched on using environment variables (AUTH_TYPE set to session_auth).
Usage:

bash
Copy code
# Start the server with session-based authentication enabled
$ API_HOST=0.0.0.0 API_PORT=5000 AUTH_TYPE=session_auth python3 -m api.v1.app
Task 2: Create a Session
Objective: Implement session creation in the SessionAuth class. This method generates a unique session ID for a user and stores it in memory.

Key Steps:
Define a class attribute user_id_by_session_id, initialized as an empty dictionary.
Implement the create_session(self, user_id: str) method:
Return None if the user_id is None or not a string.
Use the uuid module to generate a session ID.
Store the user_id and session ID pair in user_id_by_session_id.
Usage:

bash
Copy code
# Test the session creation method
$ python3 main_1.py
Task 3: User ID for Session ID
Objective: Add functionality to retrieve the user_id from a session ID.

Key Steps:
Implement the user_id_for_session_id(self, session_id: str) method:
Return None if the session_id is None or not a string.
Use the get() method to retrieve the user_id associated with the session ID in user_id_by_session_id.
Usage:

bash
Copy code
# Test retrieving the user ID from a session ID
$ python3 main_2.py
Testing
Each task includes a set of test scripts (main_0.py, main_1.py, main_2.py) to verify functionality.
The test scripts demonstrate correct session management and user retrieval for authenticated sessions.
Run the test scripts to validate each implementation.
bash
Copy code
# Example of running a test
$ python3 main_0.py
License
This project is licensed under the MIT License. See the LICENSE file for more details.

This README provides a comprehensive guide for setting up and understanding the structure of the session-based authentication system. By following the steps outlined, developers can extend the authentication system, ensuring a secure and scalable user management API.