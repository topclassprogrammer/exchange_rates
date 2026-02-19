import requests
from requests import RequestException

from logger import logger
from models import Request, Response, Session


class Exchange:
    def __init__(self, base_url, api_key, from_currency):
        self.api_key = api_key
        self.base_url = base_url
        self.from_currency = from_currency
        logger.info(f"{__class__.__name__} initialized")

    def get_exchange_rates(self):
        try:
            response = requests.get(f"{self.base_url}/{self.api_key}/latest/{self.from_currency}", verify=False)
            if 200 <= response.status_code < 300:
                logger.info(f"Connected to API: {response.url}")
                response_json = response.json()
                exchange_rates = response_json["conversion_rates"]
            else:
                exchange_rates = None
                logger.error(f"Error connecting to API. Status code: {str(response.status_code)}")
            return exchange_rates
        except RequestException as err:
            logger.error(err)

    def delete_exchange_rates(self):
        with Session() as session:
            response_objs = session.query(Response).all()
            for i in response_objs:
                session.delete(i)
            session.commit()
            logger.info(f"Deleted all rows in {Response.__tablename__}")

    def save_from_currency(self):
        with Session() as session:
            request_obj = Request(from_currency=self.from_currency)
            session.add(request_obj)
            session.commit()
            logger.info(f"Created row in {Request.__tablename__}")
            return request_obj.id

    def save_exchange_rates(self, exchange_rates: dict, request_obj_id):
        with Session() as session:
            for key, value in exchange_rates.items():
                response_obj = Response(into_currency=key, currency_value=value, request=request_obj_id)
                session.add(response_obj)
            logger.info(f"Created rows in {Response.__tablename__}")
            session.commit()
