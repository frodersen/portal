# SSO Project

## Overview

This project implements a robust Single Sign-On (SSO) solution that facilitates centralized authentication across multiple client applications. It consists of a Django-based backend, a Vue.js frontend, and multiple Express.js clients, all containerized using Docker.

## Quick Start

Follow these instructions to get the project up and running on your local machine for development and testing purposes.

### Prerequisites

- **Docker**: Ensure Docker and Docker Compose are installed on your system. For installation instructions, refer to [Docker's official documentation](https://docs.docker.com/get-docker/).

### Installation

1. **Clone the Repository**
   ```bash
   git clone https://github.com/your-github-username/sso-project.git
   cd sso-project
   ```

2. **Build and Run with Docker Compose**
   ```bash
   docker-compose up --build
   ```

## Services

- **Backend**: Accessible at http://localhost:8000. Handles all backend logic and authentication.
- **Frontend**: Accessible at http://localhost:8080. Provides the user interface for authentication.
- **Clients**: Each client application can be accessed through its specific port as configured in the Docker Compose file.

## Development

Here's how to set up your development environment:

### Backend

Navigate to the backend directory and run:

```bash
cd backend
docker build -t sso-backend .
docker run -d -p 8000:8000 sso-backend
```

### Frontend

For the frontend, navigate to its directory and execute:

```bash
cd frontend
docker build -t sso-frontend .
docker run -d -p 8080:8080 sso-frontend
```

### Clients

Set up each client by navigating to their respective directories:

```bash
cd clients/client_1
docker build -t client-1 .
docker run -d -p 3000:3000 client-1
```


