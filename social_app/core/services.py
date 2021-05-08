#!/usr/bin/python
# -*- coding: utf-8 -*-
import os
import requests


def get_pages(access_token='', uid=''):
    payload = {'access_token': access_token}
    url = 'https://graph.facebook.com/'+uid+'/accounts?access_token='+access_token
    r = requests.get(url, data=payload)
    pages = r.json()
    return pages