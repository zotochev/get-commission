# get-commission

## Description
Implementation of `get-commission` function.

### Signature:
```
get-commission(date_str: str) -> float
```

## Tests
The function is covered by sufficient number of test-cases.
Tests include:
* Proper date strings;
* Empty strings;
* Strings with wrong date format;
* Strings with proper date format but impossible dates;
* Strings that is not date;
* Wrong data type;

### Run tests
**Using pip package manager install**
1. Install dependencies
**Using pip package manager**
```
pip install -r requirements.txt
```
**Using pipenv package manager**
```
pipenv install
```
2. Run tests
```
pytest
```

## Requirements
* Python 3.7 or later
* PyTest
