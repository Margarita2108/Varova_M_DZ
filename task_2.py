import requests


def currency_rates(currency):
    currency = currency.upper()
    response = requests.get('http://www.cbr.ru/scripts/XML_daily.asp')
    response_str = response.content.decode(encoding=response.encoding)
    if currency in response_str:
        text_start = response_str[response_str.find(currency):]
        text = text_start[:response_str.find('ID=')]
        currency_info = text.split('>')
        nominal = currency_info[2].split('<')[0]
        currency_name = currency_info[4].split('<')[0].lower()
        currency_value = currency_info[6].split('<')[0]
        currency_value = float(currency_value.replace(',','.'))
        # в этом примере не вижусмысла работать с decimal
        return nominal, currency_name, currency_value


print('{0[0]} {0[1]} это {0[2]} рублей'.format(currency_rates('KGS')))
print('{0[0]} {0[1]} это {0[2]} рублей'.format(currency_rates('czk')))
print(currency_rates('USD'))
print(currency_rates('gdf'))
