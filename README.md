# Programming Assignment 1: A Barebones HTTP/1.1 Client

In this programming exercise, you will create a barebones web client. While
python includes a basic http client module `http.client`, this assignment will
serve as a learning experience for translating a protocol into an
implementation. Your deliverable will be a client which only implements the
`GET` method and follows the basics of the HTTP/1.1 specification, enough to
download files as one would with the command line program `curl`.

## HTTP/1.1 Features

[HTTP/1.0](https://tools.ietf.org/search/rfc1945) describes the most basic
functionality that an HTTP client is required to do. HTTP/1.1 includes several
new features that extend the protocol. For this assignment, you will only be
required to implement these additional features:

  * Include a `Host:` header
  * Correctly interpret `Transfer-encoding: chunked`
  * Include a `Connection: close` header, or handle persistent connections

These new features are described in James Marshall's excellent [HTTP Made Really Easy](https://www.jmarshall.com/easy/http/#http1.1clients) under the HTTP/1.1
clients subsection.

Note that the RFCs are your friends: if you're having trouble with
`Transfer-encoding`, check [the RFC][http] for hints!


## Basic HTTP functionality

As seen in class, HTTP is a stateless request-response protocol that consists
of an initial line, zero or more headers, and zero or more bytes of content.
Your program will implement a function, `retrieve_url`, which takes a url (as
a `str`) as its only argument, and uses the HTTP protocol to retrieve and
return the body's bytes (do not decode those bytes into a string). Consult
the book or your class notes for the basics of the HTTP protocol.

You may assume that the URL will not include a fragment, query string, or
authentication credentials. You are not required to follow any redirects -
only return bytes when receiving a `200 OK` response from the server. If for
any reason your program cannot retrieve the resource correctly, `retrieve_url`
should return `None`.


## Testing Script

Testing your code does not have to be a manual affair. This assignment lends
itself very well to automated testing.

We have provided a testing script for you. You will need to install the
[requests](http://docs.python-requests.org/en/master/) library to use it
(this can be done using `pip install requests`, or possibly
  `pip3 install requests`, depending on your setup). While you cannot
use `requests` to implement your assignment, you _can_ use it to test your code.

The `requests` module has far more features implemented from the HTTP spec
(and a different interface) than the code that you are implementing.

One you have `requests` installed, you can call the testing script with
`python ./hw1_test.py` (with an optional `--debug` flag to provide more
information).  The testing script will compare your implementation of the
`retrieve_url` function with a correct one, when calling a set of URLs.
You should make sure that your function is giving the output that
matches the known-correct output fetched by the testing script.

Remember, you only need to implement the features listed above. You should
probably implement the `Host:` header (important) and the `Connection: close`
header (easy) first, and then add chunked transfer encoding later. If you
have any doubts about what you can/can't use, or what you should/shouldn't
implement, ask on Piazza.


## Template

A trivial template is provided in this repository, as `hw1.py`.

## Grading

Grading will be done automatically using a script. For this assignment, we will
be providing a testing harness.  This is not guaranteed to be the method we use
for grading, but it will likely be very similar. If you wish, you can share
test cases you have written with the class. Students who share test cases
publicly will very likely receive extra participation credit.

Your program will be tested (at least) on these urls:

```python
TEST_CASES = [
    'http://www.example.com',  # most basic example
    'http://accc.uic.edu/contact',  # longer basic example
    'http://i.imgur.com/fyxDric.jpg',  # is an image
    'http://www.illinois.edu/doesnotexist',  # causes 404
    'http://www.ifyouregisterthisforclassyouareoutofcontrol.com/', # NXDOMAIN
    'http://marvin.cs.uic.edu:8080/', # nonstandard port
    'http://www.httpwatch.com/httpgallery/chunked/chunkedimage.aspx' # chunked encoding
]
```

If you're debugging a problem or simply curious, try firing up Wireshark, and
then fetch the URL both with the `requests` library or `curl` program as
well as with your code.  You'll be able to compare both requests as they
were sent, as well as the responses received.

### File Submission Requirements

You should include the following files in your repo when submitting the
assignment.  All other files will be ignored.

  * `README.md`: this file
  * `hw1.py`: python3 code that implements the function `retrieve_url`, matching
    the requirements discussed in this assignment.
  * `netid.txt`: a text file that contains only your UIC NetID.


### Points and Scoring
There is a total of **16 main points**, and **4 bonus points** on this
assignment, for a grand total of **20 possible points**.

  * **1 point** for correctly handling each of the 7 URLs mentioned above.
  * **3 points** for correctly handling each of 3 additional URLs
  * **1 bonus point** for correctly handling each of the additional
    test cases given in the `TEST_CASES_BONUS` list in the `hw1_test.py`
    testing script.
  * **1 bonus point** for submitting a `hw1.py` that is "fully compliant" with
    the `pep8` and `pylint`.  "Fully compliant" here means that `pep8` returns
    with no error messages, and `pylint` scores your code `10/10`.

Your assignment is only eligible for bonus points if you get at least 5
points.  I.e. you cannot submit a well-formatted, but completely broken,
`hw1.py` and get the bonus point.

Not correctly including the `netid.txt` file will be an automatic 0 for
the assignment.

## Allowable sources

You may not use any libraries which implement parts or the whole of the `HTTP`
specification - you must perform the basic request and response
parsing/generation yourself, as well as the chunked content encoding.

Do not import or use any python libraries, or third party code, beyond
what is imported in the skeleton / `hw1.py` file in your repo.

These resources may be useful:
  * [Python standard library documentation](https://docs.python.org/3/library/)
  * [HTTP Made Easy](https://www.jmarshall.com/easy/http/)
  * [HTTP/1.1 RFC](https://www.ietf.org/rfc/rfc2616.txt)

Using _any_ code from another source, even a single line, even with a citation,
is not allowed. This includes using any implementation code from the standard
library itself. I highly recommend not even Googling for solutions to portions
of this homework - as soon as you've seen an alternate implementation, it is
very hard to write one's own.

## Due Date
This assignment is due **Friday, September 22 at 3pm**.

**Remember**, if you don't push, we don't see it! If you push even one second
too late, your assignment won't be graded. We will be counting turnin by
push time, rather than by commit time, so please make sure to leave yourself
ample time to verify that your code has been submitted successfully.
