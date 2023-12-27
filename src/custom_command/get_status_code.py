import argparse
import requests


def main():
    parser = argparse.ArgumentParser(
        prog='get-status-code',
        description='Get status code from URL',
    )
    parser.add_argument('url', type=str, help='URL to query with a GET request')

    args = parser.parse_args()

    r = requests.get(args.url)
    print(r.status_code)


if __name__ == '__main__':
    main()
