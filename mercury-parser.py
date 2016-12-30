#! /usr/bin/env python3 #! -*- coding:utf-8 -*-

from .humantime import HumanTime

import requests

'''
@kennethreitz create maya and mercury-parser
copy and learn, write the same.
'''

MERCURY_URL = 'https://mercury.postlight.com/parser?url='

class MercuryArticle(object):
    def __init__(self, parser):
        super(MercuryArticle, self).__init__()
        self._parser = parse

        # add the parameters
        self.title = None
        self.content = None
        pass

    def __repr__(self):
        return '<MercuryArticle url={}'.format(self.url)

    def next(self):
        return self._parser.parse(self.next_page_url)

    @classmethod
    def from_dict(cls, content, parser):
        p = cls(parser)
        for k, v in content.items():
            setattr(p, k, v)

        return p

class MercuryAPI(object):
    def __init__(self, API):
        super(MercuryAPI, self).__init__()
        self._api = API
        self._session = requests.Session()

    def parse(self, url):
        self.url = '{}{}'.format(MERCURY_URL, url)
        headers = {'Content-Type': 'application/json', 'x-api-key': self._api}
        return MercuryArticle.from_dict(self._session.get(self.url, headers=headers).json(), parser=self)
