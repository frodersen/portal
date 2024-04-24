# Project Title

Provide a brief description of your project here.

## Getting Started

This guide will help you get a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

Before you begin, ensure you have the following tools installed:
- Node.js and npm: Download and install from the official Node.js website (https://nodejs.org/).
- Python: Download and install from the official Python website (https://www.python.org/).

### Installing and Running the Project

Follow these step-by-step instructions to set up your development environment:

1. Clone the repository:
   git clone https://github.com/frodersen/portal

2. Navigate to the frontend directory and install dependencies:
   cd frontend
   npm install

3. Start the frontend development server:
   npm run serve

4. In a new terminal window, set up the Python virtual environment in the backend directory:
   cd backend
   python3 -m venv myenv
   source myenv/bin/activate
   pip install -r requirements.txt

5. Start the backend server:
   python manage.py runserver

6. For each client, navigate to the client directory, install the dependencies, and start the client:
   cd clients/client_1
   npm install
   node app.js
   Repeat steps for client_2, client_3, and ntnui_client.

Now, you should have the frontend, backend, and all clients running on your local machine.

## Built With

- Vue.js - The web framework used for the frontend (https://vuejs.org/)
- Django - The web framework used for the backend (https://www.djangoproject.com/)
- Express.js - The web framework used for the clients (https://expressjs.com/)

## Contributing

Explain how others can contribute to your project.

## License

Add information about the license here.


