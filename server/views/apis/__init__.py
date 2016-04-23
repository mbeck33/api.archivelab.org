#!/usr/bin/env python
#-*-coding: utf-8 -*-

"""
    __init__.py
    ~~~~~~~~~~~
    URLs list for api

    :copyright: (c) 2015 by Internet Archive
    :license: see LICENSE for more details.
"""

from flask import render_template, request
from flask.views import MethodView
from views import rest_api
from views.apis.v1 import items, collections, search, wayback, iiif, music, \
    books, analytics, television, scholar, webtorrent
from util import domain


class Endpoints(MethodView):
    @rest_api
    def get(self, uri=None):      
        urlbase = request.base_url[:-1]
        return dict([(urls[i+1].__name__.split(".")[-1].lower(),
                      urlbase + urls[i])
                     for i in range(len(urls))[::2]]
)

urls = (
    '/items', items,
    '/search', search.Search,
    '/collections', collections,
    '/snapshots', wayback,
    '/music', music,
    '/iiif', iiif,
    '/scholar', scholar,
    '/books', books,
    '/analytics', analytics,
    '/webtorrents', webtorrent,
    '/television', television,
    '/', Endpoints
    )

