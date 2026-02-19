import os
import time
from parser import Parser

from dotenv import load_dotenv

from exchange import Exchange
from models import create_tables

if __name__ == "__main__":
    create_tables()

    parser = Parser()
    parser.add_argument("period")
    args = parser.parser.parse_args()

    load_dotenv()
    exchange = Exchange("https://v6.exchangerate-api.com/v6/", os.getenv("API_KEY"), "USD")
    exchange_rates = exchange.get_exchange_rates()
    request_obj_id = exchange.save_from_currency()
    while True:
        exchange.delete_exchange_rates()
        exchange.save_exchange_rates(exchange_rates, request_obj_id)
        time.sleep(int(args.period))
