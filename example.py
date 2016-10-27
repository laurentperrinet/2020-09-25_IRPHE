#! /usr/bin/env python3
# -*- coding: utf-8 -*-
from __future__ import division, print_function, absolute_import
__author__ = "Laurent Perrinet INT - CNRS"
__licence__ = 'BSD licence'
DEBUG = True
DEBUG = False
"""

Documentation for slides.py - serves as a template for future presentations.


"""

import os
home = os.environ['HOME']

from slides import Slides

meta = dict(
    embed = True,
    draft = DEBUG, # show notes etc
    width= 1600,
    height= 1000,
    margin= 0.1618,#
    #reveal_path = 'http://lab.hakim.se/reveal-js/', #/css/reveal.css file://' + home +  embed = True,
    reveal_path = 'http://cdn.jsdelivr.net/reveal.js/3.0.0/',
    #reveal_path = 'https://s3.amazonaws.com/hakim-static/reveal-js',
    theme='night',

    author='Laurent U Perrinet, INT',
    author_link='<a href="http://invibe.net">Laurent U Perrinet, INT</a>',
    title="""A simple way to make slideshows?""",
    short_title="What's slides.py?",
    conference="Example conference",
    Acknowledgements="""<h3>Acknowledgements:</h3>
            <ul>
                <li>Some people...</li>
                <li>Lots more people...</li>
           </ul>

""",
sections = ['Intro', 'Methods', 'Results']
)
s= Slides(meta)
figpath = 'figures/'
s.hide_slide(content=s.content_figures(
    [os.path.join(figpath, 'mire.png')], bgcolor="black",
    height=s.meta['height']*.90),
    #image_fname=os.path.join(figpath, 'mire.png'),
    notes="""
Check-list:
-----------

* (before) bring miniDVI adaptors, AC plug, remote, pointer
* (avoid distractions) turn off airport, screen-saver, mobile, sound, ... other running applications...
* (VP) open monitor preferences / calibrate / title page
* (timer) start up timer
* (look) @ audience
""")

#####################################################################################
## Intro - 5''
#####################################################################################
#####################################################################################
intro = """
<h2 class="title">{title}</h2>
<h3>{author_link}</h3>
<img src="http://blog.invibe.net/files/2016-04-25_pollymagoo/figures/troislogos.png" width=61%/>
{Acknowledgements}
<h3>{conference}</h3>
        """.format(**meta)
s.add_slide(content=intro,
            notes="""
* (AUTHOR) Hello, I am Laurent Perrinet from the Institute of Neurosciences of
la Timone in Marseille, a joint unit from the CNRS and the AMU
* (OBJECTIVE) in this short talk, I will demonstrate how to use slides.py to generate
simple slides...
* (ACKNO) and focus on content rather than on form
""")
s.close_section()
#####################################################################################
## Methods - 15''
#####################################################################################
#####################################################################################
s.open_section()
s.add_slide_outline(1)
s.add_slide_summary(
        ['Go fullscreen using the f key',
         'You can have an overlook using the o key',
         'Navigate using the arrow keys',
         'see notes using the n key'],
                      notes="""
* and write notes using markdown

""")
s.close_section()
#####################################################################################
## Results - 15''
#####################################################################################
#####################################################################################
s.open_section()
s.add_slide_outline(2)

s.add_slide(content="""
    <video controls autoplay loop width=99%/>
      <source type="video/mp4" src="{}">
    </video>
    """.format(s.embed_video(os.path.join(figpath, '00003_droplets_i_sparse_0_seed_1974.mp4'))),
    notes="""

""")
s.close_section()
#####################################################################################
s.compile(filename='example.html')
