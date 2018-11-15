# -*- coding: utf-8 -*-


class RegEntry(object):
    def __init__(self):
        self.template = ''
        self.plonecli_alias = ''
        self.depend_on = None
        self.deprecated = False
        self.info = ''


def jsonify():
    reg = RegEntry()
    reg.template = 'bobtemplates.migration:jsonify'
    reg.plonecli_alias = 'jsonify'
    return reg
