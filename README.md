# SSO Project

## Overview

This project implements a robust Single Sign-On (SSO) solution that facilitates centralized authentication across multiple client applications. It consists of a Django-based backend, a Vue.js frontend, and multiple Express.js clients, all containerized using Docker.

## Quick Start

Follow these instructions to get the project up and running on your local machine for development and testing purposes.

### Prerequisites

- **Docker**: Ensure Docker and Docker Compose are installed on your system. For installation instructions, refer to [Docker's official documentation](https://docs.docker.com/get-docker/).

### Installation

```bash
git clone https://github.com/frodersen/portal.git
cd portal
```

### Run project

```bash
docker-compose up --build
```

### Run frontend tests

```bash
docker-compose -f docker-compose.test.frontend.yml up --build
```

### Run backend tests

```bash
docker-compose -f docker-compose.test.backend.yml up --build
```
