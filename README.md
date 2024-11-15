# Expense Management System

This project is an expense management system that consist of a Streamlit frontend application and FastAPI backend server.

## Project Strcture

- **frontend/**: Contains the Streamlit application code.
- **backend/**: Contains the FastAPI backend server code.
- **tests/**: Contains the test cases for both frontend and backend.
- **requirements.txt**: Lists the required Python packages.
- **README.md**: Provides an overview and instructions for the project.

## Setup Instructions

1. **Clone the repository**:
    ```bash
    git clone https://github.com/amsowmya/Project-expense-tracking
    cd Project-expense-tracking
    ```
2. **Install dependencies**:
    ```commandline
    pip install -r requirements.txt
    ```
3. **Run the FastAPI server**:
    ```commandline
    uvicorn server.server:app --reload
    ```
4. **Run the Streamlit app**:
    ```commandline
    streamlit run frontend/app.py
    ```