# CI/CD Pipeline for Flask Application

This repository contains a Flask web application with a CI/CD pipeline set up using GitHub Actions. The pipeline automates the testing and deployment of the Flask application to an Azure VM.

## Application Overview

The Flask application (`task1.py`) is a simple web application that responds with "hello world" when accessed. It uses the Flask framework for creating the web server and routing requests.

## Setup and Installation

To run the Flask application locally, you can follow these steps:

1. Clone the repository:

   ```bash
   git clone https://github.com/your-username/your-repository.git
   ```

2. Install the required dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. Run the Flask application:

   ```bash
   python task1.py
   ```

   The application will be accessible at `http://localhost:5000`.

## CI/CD Pipeline

The CI/CD pipeline is triggered on every push to the `main` branch. It performs the following steps:

1. **Checkout code**: Checks out the code from the repository.
2. **Set up Python**: Sets up the Python environment.
3. **Install dependencies**: Installs the required Python dependencies for the application.
4. **Run tests**: Runs the unit tests using pytest to ensure the application behaves as expected.
5. **Deploy to Azure VM**: Deploys the application to an Azure VM if the tests pass.

## Environment Variables

The following environment variables are required for the deployment:

- `SSH_PRIVATE_KEY`: Private SSH key for connecting to the Azure VM.
- `SSH_PUBLIC_KEY`: Public SSH key for verifying the Azure VM's host key.

Ensure that these environment variables are set in your GitHub repository settings.

## Deployment

To deploy the application to an Azure VM, you need to update the deployment script in the GitHub Actions workflow (`main.yml`) with your Azure VM's IP address and application path. The deployment script uses SSH to connect to the Azure VM and deploy the application.


