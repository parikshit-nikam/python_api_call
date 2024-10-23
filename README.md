# PYTHON_API_CALL

## Requirements

- Python 3.8+

## Installation Steps

Follow the steps below to set up and run the project:

1. **Install Python**  
   Ensure you have Python installed on your system. You can download it from the [official Python website](https://www.python.org/downloads/).

2. **Create a Virtual Environment**  
   Navigate to your project directory and create a virtual environment:
   ```bash
   python -m venv venv
   ```

3. **Activate the Virtual Environment**
- On Windows:
    ```bash
    venv\Scripts\activate
    ```
    
- On macOS and Linux:
    ```bash
    source venv/bin/activate
    ```

4. **Install Poetry**
Install Poetry, a dependency manager for Python:
    ```bash
    pip install poetry
    ```

5. **Install Project Dependencies**
Use Poetry to install the required dependencies:
    ```bash
    poetry install
    ```

6. **Start the Poetry Shell**
Enter the Poetry shell environment:
    ```bash
    poetry shell
    ```

7. **Run the Application**
Finally, run the main application:
    ```bash
    python main.py
    ```

