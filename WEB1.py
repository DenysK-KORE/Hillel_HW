import requests
from assertpy import assert_that

urls = ('https://google.com/s', 'https://google.com/', 'https://google.com/f')


def url_check(var):
    response = requests.get(var)
    response = response.status_code
    if response == 200:
        return 1
    else:
        return 2


for i in urls:
    print(url_check(i))


def test_url_check(data='https://google.com/'):
    assert url_check(data) == 1


def test_url_check_false (data='https://google.com/s'):
    assert url_check(data) == 2


# r = url_check(urls)