# Sign Language Translation API

This project is a Django-based API that provides text translation services. The API accepts a POST request with text input in JSON format, processes the input, and returns the translated text in JSON format.

## Getting Started

Follow these steps to set up the project on your local machine.

### Prerequisites

Make sure you have the following installed on your local machine:
- Python 3.x
- Git
- pip (Python package manager)

### 1. Clone the repository

First, you need to clone the GitHub repository to your local machine. Run the following command in your terminal:

```bash
git clone https://github.com/LucaXYB/sign_languange_translation_api.git
```

### 2. Navigate to the project directory

Once the repository is cloned, navigate into the project directory:

```bash
cd sign_languange_translation_api
```

### 3. Set up a virtual environment (optional but recommended)

It's a good practice to use a virtual environment to isolate project dependencies. Run the following commands to set up and activate a virtual environment:

For macOS/Linux:

```bash
python3 -m venv venv
source venv/bin/activate
```

For Windows:

```bash
python -m venv venv
.\venv\Scripts\activate
```

### 4. Install the dependencies
Once the virtual environment is activated, install the project dependencies using the requirements.txt file:

```bash
pip install -r requirements.txt
```

This will install all the necessary libraries and packages to run the project.

### 5. Run the project

After the dependencies are installed, you can run the Django development server:

```bash
python manage.py runserver
```

This will start the server at http://127.0.0.1:8000/.

By default, the API endpoint for text translation is available at:

```bash
POST http://127.0.0.1:8000/api/translate/
```

## Testing the API

There are two ways to test this API: using Django's built-in test framework or using curl to manually send HTTP requests.

### Method 1: Using Django's built-in test framework

I finished the test code, you can use the following command to run the test suite:

```bash
python manage.py test
```

The test suite includes tests for:
1) Validating successful text translation.
2) Handling invalid JSON input.
3) Handling cases where no text is provided.
4) Ensuring only POST requests are accepted.

Expected Output

If all the tests pass, the expected output will look like this:

```bash
Creating test database for alias 'default'...
System check identified no issues (0 silenced).
....
----------------------------------------------------------------------
Ran 4 tests in 0.012s

OK
```

### Method 2: Using curl commands

You can manually test the API using curl commands from the terminal. Below are some examples:

1. Test a successful translation

```bash
curl -X POST http://127.0.0.1:8000/api/translate/ \
-H "Content-Type: application/json" \
-d '{"text": "hello"}'
```

Expected response:

```bash
{
    "input_text": "hello",
    "translated_text": "hello (translated)",
    "message": "Translation successful"
}
```

2. Test missing text input

```bash
curl -X POST http://127.0.0.1:8000/api/translate/ \
-H "Content-Type: application/json" \
-d '{}'
```

Expected response:

```bash
{
    "error": "No text provided"
}
```

3. Test invalid JSON input

```bash
curl -X POST http://127.0.0.1:8000/api/translate/ \
-H "Content-Type: application/json" \
-d 'invalid json'
```

Expected response:

```bash
{
    "error": "Invalid JSON"
}
```

4. Test invalid method (GET request)

```bash
curl -X GET http://127.0.0.1:8000/api/translate/
```

Expected response:

```bash
{
    "error": "Invalid method"
}
```

## Project Structure

Here's an overview of the project structure:

```bash
sign_language_translation_api/
├── manage.py
├── requirements.txt
├── translation/
│   ├── __init__.py
│   ├── views.py
│   ├── tests.py
│   ├── urls.py
│   ├── migrations/
```

1) manage.py: The entry point to run and manage the Django project.
2) requirements.txt: The file containing all project dependencies.
3) translation/: Contains the views, tests, and URL configurations for the API.