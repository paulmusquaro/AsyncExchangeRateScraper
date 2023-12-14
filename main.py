import aiohttp
import asyncio
import datetime
import json
import sys


async def fetch_exchange_rates(date):
    url = f"https://api.privatbank.ua/p24api/exchange_rates?json&date={date}"
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            data = await response.json()
            return data


async def get_exchange_rates_for_last_n_days(n):
    today = datetime.date.today()
    exchange_rates = []
    for i in range(n):
        date = today - datetime.timedelta(days=i)
        exchange_rate_data = await fetch_exchange_rates(date.strftime("%d.%m.%Y"))
        exchange_rate = {"EUR": None, "USD": None}

        for rate in exchange_rate_data["exchangeRate"]:
            if rate["currency"] == "EUR":
                exchange_rate["EUR"] = {
                    "sale": rate["saleRateNB"],
                    "purchase": rate["purchaseRateNB"]
                }
            elif rate["currency"] == "USD":
                exchange_rate["USD"] = {
                    "sale": rate["saleRateNB"],
                    "purchase": rate["purchaseRateNB"]
                }

        exchange_rates.append({date.strftime("%d.%m.%Y"): exchange_rate})
    return exchange_rates


if __name__ == "__main__":

    if len(sys.argv) != 2:
        print("Usage: python main.py <number_of_days>")
        sys.exit(1)

    try:
        n = int(sys.argv[1])
        if n > 10:
            print("You can only get exchange rates for up to the last 10 days.")
            sys.exit(1)
    except ValueError:
        print("Invalid input. Please provide a valid number of days.")
        sys.exit(1)

    loop = asyncio.get_event_loop()
    exchange_rates_data = loop.run_until_complete(get_exchange_rates_for_last_n_days(n))

    print(json.dumps(exchange_rates_data, indent=2))