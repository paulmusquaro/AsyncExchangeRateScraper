# AsyncExchangeRateScraper


This project fetches the exchange rates for EUR and USD from the PrivatBank API for the last N days asynchronously. It uses Python’s `aiohttp` for making asynchronous HTTP requests and `asyncio` for handling concurrency, allowing for efficient fetching of data without blocking execution.

## Features
- Fetches exchange rates for EUR and USD for the last N days.
- Fetches exchange rates asynchronously using `aiohttp` and `asyncio`.
- Displays the exchange rates in a JSON format for easy parsing.

## Requirements
- Python 3.6 or higher
- `aiohttp` (for asynchronous HTTP requests)

You can install the required dependencies using pip:
```bash
pip install aiohttp
```

## Usage
To use this script, run it from the command line and pass the number of days as an argument. For example, to fetch exchange rates for the last 5 days, run the following command:

```bash
python main.py 5
```

**Note**: You can only fetch exchange rates for up to 10 days at a time.

### Command-line arguments
- `<number_of_days>`: The number of days you want to fetch the exchange rates for (maximum 10 days).

## Example Output
```json
[
  {
    "05.02.2025": {
      "EUR": {
        "sale": 40.15,
        "purchase": 39.85
      },
      "USD": {
        "sale": 37.50,
        "purchase": 37.20
      }
    }
  },
  {
    "04.02.2025": {
      "EUR": {
        "sale": 40.10,
        "purchase": 39.80
      },
      "USD": {
        "sale": 37.45,
        "purchase": 37.15
      }
    }
  }
]
```

## How It Works
1. The script takes the number of days as an input argument.
2. It retrieves the exchange rates for EUR and USD for each of the last N days by querying the PrivatBank API asynchronously.
3. The data is returned in a JSON format with the sale and purchase rates for each currency on each day.

## License
This project is open-source and available under the MIT License. Feel free to submit issues or pull requests if you find any bugs or want to add new features!
