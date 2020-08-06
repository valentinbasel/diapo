#! /usr/bin/env python
# -*- coding: utf-8 -*-
###############################################################################
# parser.py
# Copyright © 2016 valentinbasel@gmail.com
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
###############################################################################

from docutils import core
from docutils.writers.html4css1 import Writer,HTMLTranslator
# import HTMLParser
from html.parser import HTMLParser

class HTMLParserModule(HTMLParser):
    tag=None
    
    def __init__(self,diapo):
        """docstring for fname"""
        HTMLParser.__init__(self)
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
            if data != "\n":
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
        #print(cad)
        parsed = self.htmltag(self.diapo)
        p = parsed.feed(cad.decode("utf-8"))
        #print (help(parsed.feed))
