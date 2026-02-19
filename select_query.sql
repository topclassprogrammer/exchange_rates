SELECT from_currency, into_currency, currency_value
FROM requests
JOIN responses ON requests.id = responses.request;