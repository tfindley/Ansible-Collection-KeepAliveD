#!/bin/python3

# import os
import requests
import click
import sys
import json

@click.command()
@click.option('-u', '--url', envvar='URL', help='URL to query', required=True)
@click.option('-f', '--field', envvar='FIELD', help='JSON field you wish to query', required=True)
@click.option('-r', '--response', envvar='RESPONSE', help='JSON value you wish to check for', required=True)
@click.option('-t', '--timeout', envvar='TIMEOUT', help='Timeout for the HTTP request', default='5', required=False)
@click.option('-q', '--quiet', is_flag=True, help='Suppress output except for errors')

def main(url, field, response, timeout, quiet):

    EXIT_OK = 0
    EXIT_BAD_RESPONSE = 1
    EXIT_ERROR = 2

    HEADERS = {
        "Content-Type": "application/json",

    }

    try:
        data = requests.get(url = url, headers = HEADERS, timeout = int(timeout)).json()

        if not quiet:
            print(json.dumps(data, indent=2))

        if field not in data:
            print(f"Error: '{field}' field is missing from the response.")
            sys.exit(EXIT_ERROR)


        if data.get(field) == response:
            if not quiet:
                print(f"OK: '{response}' was found in '{field}'. Exiting with 0")
            sys.exit(EXIT_OK)
        else:
            if not quiet:
                print(f"BAD RESPONSE: '{response}' was not found in '{field}'. Exiting with 1")
            sys.exit(EXIT_BAD_RESPONSE)

    except requests.exceptions.RequestException as e:
        print(f"Request Failed: {e}")
        sys.exit(EXIT_ERROR)

    except ValueError as e:
        print(f"Invalid JSON: {e}")
        sys.exit(EXIT_ERROR)


if __name__ == '__main__':
    main()