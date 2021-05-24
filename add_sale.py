def main(argv):
    prices = argv[1:]
    with open(file_prise, 'a', encoding='utf-8') as f:
        for price in prices:
            f.write(price+'\n')
    return


file_prise = 'bakery.csv'
if __name__ == '__main__':
    import sys

    main(sys.argv)
