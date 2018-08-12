#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2015 valentin <valentin@localhost.localdomain>
#
# Distributed under terms of the MIT license.

"""

"""
from docutils import core
from docutils.writers.html4css1 import Writer,HTMLTranslator
import HTMLParser


class HTMLParserModule(HTMLParser.HTMLParser):
    tag=None
    
    def __init__(self,diapo):
        """docstring for fname"""
        HTMLParser.HTMLParser.__init__(self)
        self.diapo=diapo

    def handle_starttag(self, tag, attrs):

        self.tag=tag
        self.attrs=attrs
    def handle_endtag(self, tag):
        self.endtag=tag
        if self.endtag=="strong":
            self.tag="p"

    def handle_data(self, data):
        start=self.tag
        #print start
       # if start=="pre" and self.endtag=="pre":
        #    print "encontre el video y me preparo a parsearlo"
         #   print data



           # self.endtag==""
           # return

        if start=="h2":
        #    if data <>"\n":
            self.diapo.title(data)
            return
        if start=="img" and self.endtag=="img":
            #print self.attrs 
            self.diapo.image(self.attrs)
            self.endtag==""
            return
        if start=="li":
            self.diapo.list_text(data)
        if start=="h1":
            if data <>"\n":
                self.diapo.add(data)
                return
        elif start=="p":
            #if data <>"\n":
            self.diapo.text(data)
            return
        elif start=="strong": 
            #if data <>"\n":
            self.diapo.bold(data)
            return
        else:
            return


class HTMLRstTranslator( HTMLTranslator ):
    def __init__( self, document ):
        HTMLTranslator.__init__( self, document )
        self.head_prefix = ['','','','','']
        self.body_prefix = []
        self.body_suffix = []
        self.stylesheet = []
    def astext(self):
        return ''.join(self.body)

class ParserGenerator(HTMLParserModule,HTMLRstTranslator):
    def __init__(self,diapo):
            self.diapo=diapo
            self.html_fragment_writer = Writer()
            self.html_fragment_writer.translator_class = HTMLRstTranslator
            self.htmltag=HTMLParserModule
            

    def reST_to_html( self,s ):
        return core.publish_string( s, writer = self.html_fragment_writer )

    def parsed_diapo(self,txt):
        """docstring for fname"""
        cad= self.reST_to_html(txt)
        #print cad
        parsed = self.htmltag(self.diapo)
        parsed.feed(cad)
        #print help(parsed.feed)
