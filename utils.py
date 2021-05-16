from requests import get
import time


def currency_rates(currency):
    currency = currency.upper()
    response = get('http://www.cbr.ru/scripts/XML_daily.asp')
    response_str = response.content.decode(encoding=response.encoding)
    date_res = time.strptime(response_str.split('"')[5], '%d.%m.%Y')
    date_str = response_str.split('"')[5]
    if currency in response_str:
        text_start = response_str[response_str.find(currency):]
        text = text_start[:response_str.find('ID=')]
        currency_info = text.split('>')
        nominal = currency_info[2].split('<')[0]
        currency_name = currency_info[4].split('<')[0].lower()
        currency_value = currency_info[6].split('<')[0]
        currency_value = float(currency_value.replace(',', '.'))/float(nominal)
        return currency_name, currency_value, date_str, date_res
