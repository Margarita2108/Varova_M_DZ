import re


def file_parsing(file):
    RE_PARSING = re.compile(
        r'(?P<remote_addr>[0-9,.]{7,15}|[a-z,0-9,:]{38}) - - \['
        r'(?P<request_datetime>.+?)\] "'
        r'(?P<request_type>[^"]{3,5}) \/'
        r'(?P<requested_resource>[^ \/].*) HTTP\/1.1" '
        r'(?P<response_code>[^\/1.1" ][0-9]{1,3}) '
        r'(?P<response_size>[0-9]{1,3})'
    )

    with open(file, 'r', encoding='utf-8') as file:
        for line_str in file:
            parsed_raw = RE_PARSING.findall(line_str)
            print(parsed_raw)
    return


if __name__ == '__main__':
    file_parsing('nginx_logs.txt')
