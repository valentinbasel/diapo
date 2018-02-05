#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2015 valentin <valentin@localhost.localdomain>
#
# Distributed under terms of the MIT license.

"""

"""
import svgwrite
import xml.etree.ElementTree as ET
from xml.dom import minidom
import os
class SvgMain(object):
    """SgvMain"""
    def __init__(self,w,h,imgx,imgy,fontsize,background,fontfamily):

        super(SvgMain, self).__init__()
        #self.arg = arg
        self.fontsize=fontsize
        self.h=h
        self.w=w
        self.background=background
        self.fontfamily=fontfamily
        self.imgx=imgx
        self.imgy=imgy
        self.svg_document = svgwrite.Drawing('',size = (w, h))
        self.yfont=self.fontsize+100
        self.xfont=0

    def add_image(self,x,y,w,h,img):
        """docstring for fname"""
        image =self.svg_document.image(img,
                                        insert=(x+self.imgx,y+self.imgy),
                                        size=(w,h))
        self.svg_document.add(image)

    def add_background_image(self,x,y,img):
        """docstring for fname"""
        image =self.svg_document.image(img, insert=(x,y), size=(self.w,self.h))
        self.svg_document.add(image)

    def add_rect(self,x,y,idrect):
        """docstring for add_diapo"""
        rgb="rgb(" + self.background + ")"
        self.svg_document.add(self.svg_document.rect(insert = (x, y),
                                                size = (self.w, self.h),
                                                stroke_width = "0",
                                                stroke = "black",
                                                fill = rgb,id=str(idrect)
                                                ))
        self.yfont=self.fontsize+100
        self.xfont=0

    def add_circle(self,x,y,color):
        """docstring for add_diapo"""
        #rgb="rgb(" + color + ")"
        self.svg_document.add(self.svg_document.circle(center=(x, y),
                                                r=int(self.fontsize)/4,
                                                stroke_width = "0",
                                                fill=color
                                                ))

    def add_text(self,txt,x,y,color):
        """docstring for add_text"""
        text_style = ("font-size:%ipx; font-family:%s" % 
                        (int(self.fontsize), self.fontfamily)) 
        cad=txt.split("\n")
        for txtsplit in cad:
            #print txtsplit
            self.svg_document.add(
                            self.svg_document.text(
                                        txtsplit,
                                        insert = (x,y),
                                        style=text_style,
                                        fill=color)
                                )
            y+=self.fontsize
        return y

    def add_bold(self,txt,x,y,color):
        """docstring for add_text"""

        text_style = ("font-size:%ipx; font-family:%s" % 
                            (int(self.fontsize), self.fontfamily)) 
        svg_span = self.svg_document.text("")
        self.svg_document.add(svg_span)
        svg_span.add(self.svg_document.tspan(txt, insert =
        (x,y),style=text_style,font_weight="bold",fill=color))

    def add_title(self,txt,x,y,color):
        """docstring for add_text"""
        text_style = ("font-size:%ipx; font-family:%s" % 
                        (int(self.fontsize*2), self.fontfamily)) 
        svg_span = self.svg_document.text("")
        self.svg_document.add(svg_span)
        svg_span.add(self.svg_document.tspan(txt, insert =
        (x,y),style=text_style,font_weight="bold",fill=color))

    def add_ns1(self,idrect,idiapo,namediapo):
        """docstring for fname"""
        ns1=ET.Element('ns1:frame')
        ns1.set('id','frame'+namediapo)
        ns1.set('ns1:transition-path-hide',"true")
        ns1.set('ns1:transition-profile',"linear")
        ns1.set('ns1:transition-zoom-percent',"0")
        ns1.set('ns1:transition-duration-ms',"1000")
        ns1.set('ns1:timeout-ms',"5000")
        ns1.set('ns1:timeout-enable',"false")
        ns1.set('ns1:show-in-frame-list',"true")
        ns1.set('ns1:clip',"true")
        ns1.set('ns1:hide',"true")
        ns1.set('ns1:sequence',str(idrect))
        ns1.set('ns1:title',namediapo)
        ns1.set('ns1:refid',str(idiapo))
        self.xml_content.append(ns1)

    def add_script(self):
        """docstring for fname"""
        js=open(os.path.join(os.path.dirname(__file__), "json/sozi.min.js")).read()
        cs=open(os.path.join(os.path.dirname(__file__), "css/sozi.min.css")).read()

        scr=self.svg_document.script()
        sty=self.svg_document.style()
        scr.append(js)
        sty.append(cs)
        self.svg_document.add(scr)
        self.svg_document.add(sty)
    def prepare_xml(self):
        """docstring for fname"""
        self.add_script()
        self.xml_content = self.svg_document.get_xml()
        self.xml_content.attrib['xmlns:ns1']="http://sozi.baierouge.fr"

  
    def save_svg(self,namesvg,dat_ns1):
        """docstring for save_svg"""
        self.prepare_xml()
        for idrect,idiapo,namediapo in dat_ns1: 
            self.add_ns1(idrect,idiapo,namediapo)
        cad=str( ET.tostring(self.xml_content))
        reparsed = minidom.parseString(cad)
        doc=reparsed.toprettyxml(indent="  ")
        file=open(namesvg,"w")
        file.write(doc.encode('utf-8'))
        file.close()


