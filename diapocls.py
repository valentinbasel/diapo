#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2015 valentin <valentin@localhost.localdomain>
#
# Distributed under terms of the MIT license.

"""

"""

from svgcomposer import SvgMain

class Diapo(object):
    """docstring for ClassName"""
    def __init__(self,conf):
        super(Diapo, self).__init__()
        self.dat_ns1=[]
        self.id_diapo=0
        self.x=0
        self.y=0
        self.marginx=int(conf["marginx"])
        self.marginy=int(conf["marginy"])
        self.h=int(conf["height"])
        self.w=int(conf["width"])
        self.titlex=int(conf["titlex"])
        self.titley=int(conf["titley"])
        self.imgx=int(conf["imgx"])
        self.imgy=int(conf["imgy"])
        self.fontcolor=conf["fontcolor"]
        self.fontsize=int(conf["fontsize"])
        self.background=conf["background"]
        self.backgroundimg=conf["backgroundimg"]
        self.backgroundimg2=conf["backgroundimg2"]
        self.fontfamily=conf["fontfamily"]
        self.titlefontcolor=conf["titlefontcolor"]
        self.SVG=SvgMain(
                            (str(self.w)+"px"),
                            (str(self.h)+"px"),
                            self.imgx,
                            self.imgy,
                            self.fontsize,
                            self.background,
                            self.fontfamily
                            )

    def add(self,namediapo):
        """docstring for fname"""
        self.x=self.x+self.w+10

        self.y=0#self.y+self.h+10

        self.SVG.add_rect(self.x,self.y,self.id_diapo)
        self.SVG.add_rect(self.x,self.y,str(self.id_diapo)+"rec")
        self.SVG.add_background_image(self.x,self.y,self.backgroundimg)
        self.SVG.add_background_image(self.x,self.y,self.backgroundimg2)
        self.dat_ns1.append((self.id_diapo,self.id_diapo,namediapo))
        self.id_diapo+=1
        self.ytxt=self.fontsize+self.marginy

    def image(self,img):
        """docstring for fname"""
        src=img[1][1]
        style=img[2][1]
        ximg=style.split(";")
        ximgend=ximg[0].replace("width: ","")
        ximgend=ximgend.replace("px","")        
        ximgend=ximgend.replace(" ","")
        yimg=style.split(";")
        yimgend=yimg[1].replace("height: ","")
        yimgend=yimgend.replace("px","")        
        yimgend=yimgend.replace(" ","")
        if src.find("video::")>-1:
            self.video(img)
            return 0
        self.SVG.add_image( self.x+self.marginx,
                            self.y+self.ytxt+self.marginy-110,
                            int(ximgend),
                            int(yimgend),
                            src)
        self.ytxt+=int(yimgend)+self.marginy+self.fontsize

    def video(self,img):
        src=img[1][1]
        style=img[2][1]
        ximg=style.split(";")
        ximgend=ximg[0].replace("width: ","")
        ximgend=ximgend.replace("px","")        
        ximgend=ximgend.replace(" ","")
        yimg=style.split(";")
        yimgend=yimg[1].replace("height: ","")
        yimgend=yimgend.replace("px","")        
        yimgend=yimgend.replace(" ","")
        src1=src.split("video::")
        src_v=src1[1]
        #print src_v
        #print int(ximgend),"---",int(yimgend)
        #print self.x+self.marginx
        #print self.y+self.ytxt+self.marginy-110,
        self.SVG.add_video( self.x+self.marginx,
                            self.y+self.ytxt+self.marginy-110,
                            int(ximgend),
                            int(yimgend),
                            src_v)



    def text(self,text):
        """docstring for fname"""
        textlen=int(len(text))
        self.ytxt= self.SVG.add_text(
                                    text,self.x+self.marginx,
                                    self.ytxt+self.marginy,
                                    self.fontcolor
                                    )

    def list_text(self,text):
        """docstring for fname"""
        textlen=int(len(text))
        if text<>"\n":
            self.SVG.add_circle(self.x+self.marginx+20,
                            self.y+self.ytxt+self.marginy-7,
                            self.fontcolor
                            )

        self.ytxt= self.SVG.add_text(
                                    text,self.x+self.marginx+30,
                                    self.y+self.ytxt+self.marginy,
                                    self.fontcolor
                                    )
        self.ytxt=self.ytxt-self.y-25


    def title(self,text):
        """docstring for fname"""
        textlen=int(len(text))
        #print textlen*self.fontsize
        self.SVG.add_title(
                    text,self.x+self.marginx+self.titlex,
                    self.y+self.ytxt+self.fontsize+self.marginy+self.titley,
                    self.titlefontcolor
                    )
        self.ytxt+=self.fontsize*2+self.marginy

    def bold(self,text):
        """docstring for fname"""
        textlen=int(len(text))
        #print textlen*self.fontsize
        self.SVG.add_bold(  text,
                            self.x+self.marginx,
                            self.y+self.ytxt,
                            self.fontcolor
                            )
        #self.ytxt+=self.fontsize-self.marginy

    def save(self,name):
        """docstring for fname"""
        try:
            self.SVG.save_svg(name,self.dat_ns1)
            print "the file ",name," was created successfully."
        except Exception, e:
            print "save error"
            exit(1)
            raise e

