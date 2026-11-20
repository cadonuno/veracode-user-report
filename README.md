# veracode-user-report

## Overview

This script retrieves users from the Veracode Identity APIs and exports their
account details to an Excel workbook named `users.xlsx` in the current working
directory.

## Requirements

- Python 3.8 or later
- Veracode API credentials configured for `veracode-api-py`
    - These API credentials need to have Administrator or Admin API 

Install the Python dependencies:

```bash
pip install -r requirements.txt
```

## Usage

Run the script from the project directory:

```bash
python user-report.py
```

The generated `users.xlsx` file is overwritten each time the script runs.