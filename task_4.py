import utils
import time

currency = 'USD'
print('На {0[2]} {0[0]} это {0[1]} рублей.'.format(utils.currency_rates(currency)))
