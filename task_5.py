def main(argv):
    for currency in argv:
        result = utils.currency_rates(currency)
        print(result[1], end=", ")
        print(result[2])
    return


if __name__ == '__main__':
   import sys
   import utils

   exit(main(sys.argv[1:]))
