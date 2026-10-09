# Product Vision and Scrum Sprint Documentation

## 1. Product Vision

**Vision Statement:** To make everyday mathematics instant, stress-free, and accessible to anyone, anywhere, at any time.

---

## 2. Product Backlog

The product backlog contains the user stories, acceptance criteria, and estimated story points for the calculator application.

### User Story 1: Addition

**User Story:** As a user, I want to add two numbers so that I can calculate their sum.

**Story Points:** 1

**Acceptance Criteria:**

* **Given** two valid numbers, **when** I select addition, **then** the calculator displays their sum.
* **Given** two positive numbers, **when** I add them, **then** the correct result is displayed.
* **Given** positive and negative numbers, **when** I add them, **then** the correct result is displayed.
* **Given** decimal numbers, **when** I add them, **then** the correct result is displayed.

### User Story 2: Subtraction

**User Story:** As a user, I want to subtract one number from another so that I can calculate their difference.

**Story Points:** 1

**Acceptance Criteria:**

* **Given** two valid numbers, **when** I select subtraction, **then** the calculator displays their difference.
* **Given** two positive numbers, **when** I subtract them, **then** the correct result is displayed.
* **Given** positive and negative numbers, **when** I subtract them, **then** the correct result is displayed.
* **Given** decimal numbers, **when** I subtract them, **then** the correct result is displayed.

### User Story 3: Multiplication

**User Story:** As a user, I want to multiply two numbers so that I can calculate their product.

**Story Points:** 1

**Acceptance Criteria:**

* **Given** two valid numbers, **when** I select multiplication, **then** the calculator displays their product.
* **Given** a number and zero, **when** I multiply them, **then** the result is `0`.
* **Given** positive and negative numbers, **when** I multiply them, **then** the correct result is displayed.
* **Given** decimal numbers, **when** I multiply them, **then** the correct result is displayed.

### User Story 4: Division

**User Story:** As a user, I want to divide one number by another so that I can calculate their quotient.

**Story Points:** 2

**Acceptance Criteria:**

* **Given** two valid non-zero numbers, **when** I select division, **then** the calculator displays their quotient.
* **Given** a dividend that is not evenly divisible by the divisor, **when** I perform the division, **then** the calculator displays the correct decimal result.
* **Given** positive and negative numbers, **when** I divide them, **then** the correct result is displayed.
* **Given** zero as the dividend and a non-zero divisor, **when** I divide, **then** the result is `0`.
* **Given** zero as the divisor, **when** I attempt to divide, **then** the calculator displays an appropriate error message and does not produce a numerical result.

### User Story 5: Exponentiation

**User Story:** As a user, I want to raise a number to a power so that I can calculate the result of exponentiation.

**Story Points:** 2

**Acceptance Criteria:**

* **Given** a valid base and exponent, **when** I select exponentiation, **then** the calculator displays the correct result.
* **Given** a positive integer exponent, **when** I raise a number to that exponent, **then** the correct result is displayed.
* **Given** an exponent of zero, **when** I raise a non-zero number to that power, **then** the result is `1`.
* **Given** a negative base and an integer exponent, **when** I perform exponentiation, **then** the correct result is displayed.
* **Given** a decimal base, **when** I raise it to a valid exponent, **then** the correct result is displayed.

---

## 3. Sprint 1

### 3.1 Selected User Stories

The following user stories were selected for Sprint 1:

* User Story 1: Addition
* User Story 2: Subtraction
* User Story 3: Multiplication

### 3.2 Sprint Review: Work Delivered

* Developed a calculator application supporting addition, subtraction, and multiplication.
* Created an automated test suite using `pytest`.
* Configured a GitHub Actions continuous integration (CI) pipeline.

### 3.3 Sprint Retrospective

#### What Went Well

* Developed the calculator functionality and created automated tests using `pytest`.
* Successfully configured GitHub Actions to run automated tests on the configured GitHub events.
* Practised using Git branches and pull requests to manage changes.
* Gained a better understanding of how Continuous Integration helps detect problems before code is merged.

#### What Could Have Gone Better

* Understanding when GitHub Actions triggers a workflow required additional troubleshooting, particularly around branches and pull requests.
* The initial CI failure highlighted the importance of inspecting workflow logs and identifying the root cause rather than making assumptions about what went wrong.
* Testing and CI configuration could have been planned and verified earlier in the sprint.

#### What Will We Improve in the Next Sprint?

* Improve project documentation.
* Expand test coverage.

---

## 4. Sprint 2

### 4.1 Sprint Review: Work Delivered

* Added division and exponentiation to the calculator.
* Expanded the automated test suite.
* Introduced basic logging and monitoring.
* Improved project documentation.

### 4.2 Sprint Retrospective

#### What Went Well

* Extended the calculator with division and exponentiation.
* Expanded the automated test suite to cover new functionality and edge cases.
* Continued using Git branches, pull requests, and GitHub Actions to validate changes.
* Introduced basic logging to make calculation behaviour and errors easier to investigate.

#### Challenges and Lessons Learned

* Adding new operations requires testing both normal inputs and edge cases.
* Automated tests help identify regressions when the application changes.
* Logging provides useful information when investigating errors.
* Continuous Integration provides an additional verification step before changes are merged.

#### What Will We Improve in the Next Sprint?

* Expand test coverage further.
* Strengthen the CI quality gate.
* Improve error handling and observability.
