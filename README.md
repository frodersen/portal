# SSO Project

Upon completion, this project will have developed a Proof-of-Concept consisting of a central Single Sign-On (SSO) application and a sample application to demonstrate the integration process. The final product is intended to be put into production and used starting from autumn 2024.

## Getting Started

This guide will help you get a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

Before you begin, ensure you have the following tools installed:

- Node.js and npm: Download and install from the official Node.js website (https://nodejs.org/).
- Python: Download and install from the official Python website (https://www.python.org/).

### Installing and Running the Project

Follow these step-by-step instructions to set up your development environment:

1. Clone the repository:
    ```
    git clone https://github.com/frodersen/portal
    ```

2. Set up the Python virtual environment for the backend:
    - Open a command prompt or terminal.
    - Navigate to the backend directory of your project:
      ```
      cd portal/backend
      ```
    - Create the virtual environment:
      ```
      python -m venv myenv
      ```
    - Activate the virtual environment:
      ```
      .\myenv\Scripts\activate
      ```

3. Set up the Backend:
    - Ensure you are in the backend directory where manage.py is located:
      ```
      cd portal
      ```
    - Start the Django development server:
      ```
      python manage.py runserver
      ```

4. Set up the Frontend:
    - Open a new command prompt or terminal window.
    - Navigate to the frontend directory:
      ```
      cd ../frontend
      ```
    - Install dependencies including Axios:
      ```
      npm install
      npm install axios
      ```
    - Start the frontend development server:
      ```
      npm run serve
      ```

5. Set up a Client:
    - Open a new command prompt or terminal window.
    - Navigate to the client's directory:
      ```
      cd ../clients/client_1
      ```
    - Install necessary dependencies:
      ```
      npm install
      ```
    - Start the client application:
      ```
      node app.js
      ```

### Built With

- Vue.js - The web framework used for the frontend (https://vuejs.org/)
- Django - The web framework used for the backend (https://www.djangoproject.com/)
- Express.js - The web framework used for the clients (https://expressjs.com/)

