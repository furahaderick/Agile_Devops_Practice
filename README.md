# Python Calculator

A simple command-line calculator built with Python that supports basic arithmetic operations and exponentiation, with automated testing and continuous integration.

## Features

* Addition
* Subtraction
* Multiplication
* Division
* Exponentiation
* Automated testing with `pytest`
* Application health check
* Continuous integration with GitHub Actions

## Getting Started

### 1. Installation

Install the required dependencies:

```bash
pip install -r requirements.txt
```

### 2. Run the Application

Start the calculator:

```bash
python calculator.py
```

## Testing

Run the automated test suite to verify that the calculator works as expected:

```bash
pytest -v
```

## Health Check

Check whether the application is functioning correctly:

```bash
python calculator.py --health
```

**Expected output:**

```text
OK
```

## Continuous Integration

### GitHub Actions

The GitHub Actions workflow automatically:

1. Checks out the repository.
2. Sets up the Python environment.
3. Installs the required dependencies.
4. Runs automated tests using `pytest`.

**Workflow triggers:**

* Pushes to the `main` branch.
* Pull requests targeting the `main` branch.

The workflow reports whether the automated tests pass or fail, helping maintain code quality and reliability.

---

*Built with Python · Tested with pytest · Automated with GitHub Actions*
