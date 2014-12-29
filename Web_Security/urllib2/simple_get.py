#!/usr/bin/env python

__author__ = "bt3"

import urllib2

def get(url):
    msg = urllib2.urlopen(url)
    print msg.read()

def get_user_agent(url):
    headers = {}
    headers['User-Agent'] = 'Googlebot'

    request = urllib2.Request(url, headers=headers)
    response = urllib2.urlopen(request)

    print response.read()
    response.close()



if __name__ == '__main__':
    HOST = 'http://www.google.com'
    get_user_agent(HOST)