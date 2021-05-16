import requests
import time


def currency_rates(currency):
    currency = currency.upper()
    response = requests.get('http://www.cbr.ru/scripts/XML_daily.asp')
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
        currency_value = float(currency_value.replace(',', '.'))
        return date_str, nominal, currency_name, currency_value, date_res


print('На {0[0]} {0[1]} {0[2]} это {0[3]} рублей'.format(currency_rates('AMD')))
print('На {0[0]} {0[1]} {0[2]} это {0[3]} рублей'.format(currency_rates('brl')))
print(currency_rates('USD'))
print(currency_rates('gdf'))
