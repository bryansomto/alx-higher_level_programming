#!/usr/bin/python3
""" a Python script that fetches https://alx-intranet.hbtn.io/status """

if __name__ == '__main__':
    from urllib import request

    with request.urlopen('https://alx-intranet.hbtn.io/status') as res:
        html = res.read()
        print('Body response:')
        print('\t- type: {}'.format(type(html)))
        print('\t- content: {}'.format(html))
