import sys
import logging

logging.basicConfig(level=logging.INFO, format="%(levelname)s:%(name)s:%(message)s")


logger = logging.getLogger(__name__)


def main():
    if "--health" in sys.argv:
        print("OK")
        return


def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    if b == 0:
        logger.error("Division by zero attempted")
        raise ZeroDivisionError("Cannot divide by zero")
    logger.info("Division completed successfully")
    return a / b


def exponentiate(a, b):
    return a**b


if __name__ == "__main__":
    main()
