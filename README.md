# Flask-API for financial data

A simple Flask API for retrieving scraped financial data from web crawler in JSONL format.

## Status

![Status](https://img.shields.io/badge/Status-Productive-green)

## Features

*   **GET /stock:** Retrieves all financial data in JSONL format.
*   **POST /stock:** Also retrieves all financial data in JSONL, it can also be used
*   **DELETE /stock:** Deletes all financial data in the jsonl file (Warning: irrevocably!).

## Installation

1.  Clone the repository:
    ```cmd
    git clone https://github.com/<DEIN_USERNAME>/<DEIN_REPO_NAME>.git
    ```
2.  Change to the project directory:
    ```cmd
    cd <DEIN_REPO_NAME>
    ```

3.  Install the required dependencies:
    ```cmd
    pip install flask
    ```

4.  Start the API:
    ```cmd
    python app.py
    ```

## Use
I use it mainly to retrieve the scraped data that I provide with my web crawler project on a remote Ubuntu server 
locally on my PC. Then I can later analyze the data with my analyzer project.

### GET /stock

Retrieves all financial data.

**Beispiel (Python):**

```python
import requests

response = requests.get('http://<SERVER_IP>:5000/stock')
data = response.json()
print(data)
```

## Tests

The API is tested with Pytest. Both the basic endpoints (GET, POST, DELETE) and the
combination of the sequence of requests against the endpoints are tested.

**Notice:** The tests currently use mainly real data. The use of mock data to isolate the tests is planned and will be 
improved in future releases.

To run the tests, first install Pytest:

```cmd
pip install pytest
```

Then navigate to the root directory of the project and run the tests:

```cmd
pytest
```
The test results are displayed in the terminal.
