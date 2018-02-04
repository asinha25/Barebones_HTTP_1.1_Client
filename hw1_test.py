'''
test cases for a simple http client.
'''
import logging
import sys
from urllib.parse import urlparse

# from hw1 import retrieve_url
from hw1 import retrieve_url

import requests

TEST_CASES = ['http://www.example.com',  # most basic example (with no slash)
              'http://accc.uic.edu/contact',  # another basic example
              'http://i.imgur.com/fyxDric.jpg',  # is an image
              'http://illinois.edu/doesnotexist',  # causes 404
              'http://www.ifyouregisterthisforclassyouareoutofcontrol.com/', # NXDOMAIN
              'http://marvin.cs.uic.edu:8080/', # nonstandard port
              'http://www.httpwatch.com/httpgallery/chunked/chunkedimage.aspx' # chunked encoding
             ]

TEST_CASES_BONUS = ['http://bits-cluster-1.research.uicbits.net/🐻.🐷',  # utf-8 in the url
                    'https://www.cs.uic.edu/~ckanich/',  # https
                    'http://www.fieggen.com/shoelace'  # redirects to trailing slash
                   ]


def retrieve_url_bonus(url):
    '''
    https, redirects, utf-8 in urls!
    '''

    response = requests.get(url)
    if response.status_code == 200:
        return response.content
    else:
        return None


def retrieve_url_oracle(url):
    '''
    the easiest way to complete this assignment. too bad you can't use it.
    '''

    scheme = urlparse(url).scheme
    if scheme != 'http':
        return None
    response = requests.get(url, allow_redirects=False)
    if response.status_code == 200:
        return response.content
    else:
        return None


def compare_output(url, oracle=retrieve_url_oracle):
    '''
    compare hw2.py output with requests output for ::url::
    '''
    try:
        # download the same page twice to check for dynamic content
        correct_output = oracle(url)
        dynamic_output = oracle(url)
        if correct_output != dynamic_output:
            print("this is a dynamic page, skipping: {}".format(url))
            return
    except requests.RequestException as exc:
        logging.debug(
            "something went wrong downloading the page: %s", type(exc).__name__)
        correct_output = None

    try:
        student_output = retrieve_url(url)
    except Exception as exc: # pylint: disable=broad-except
        print("uncaught exception ({}) for {}".format(type(exc).__name__, url))
        return
    if correct_output == student_output:
        print("correct output for {}".format(url))
    else:
        print("incorrect output for {}".format(url))

def main(args):
    if "--debug" in args:
        logging.basicConfig(level=logging.DEBUG)

    for testcase in TEST_CASES:
        compare_output(testcase)

    print("and for style points...")
    for testcase in TEST_CASES_BONUS:
        compare_output(testcase, oracle=retrieve_url_bonus)



if __name__ == "__main__":
    main(sys.argv[1:])
