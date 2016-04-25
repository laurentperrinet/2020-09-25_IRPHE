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
    draft = DEBUG, # show notes etc
    width= 1600,
    height= 1000,
    margin= 0.,#1618,
    reveal_path = 'http://lab.hakim.se/reveal-js/', #/css/reveal.css file://' + home + '/pool/libs/numbers/ipython_slides/reveal.js/',
    theme='night',
    author='Laurent U Perrinet, INT',
    author_link='<a href="http://invibe.net">Laurent U Perrinet, INT</a>',
    title="""A simple way to make slideshows?""",
    short_title="What's slides.py?",
    conference="Example conference",
    Acknowledgements="""<h3>Acknowledgements:</h3>
            <ul>
                <li>Lots of people...</li>
           </ul>

""",
sections = ['TOTO']
)
s= Slides(meta)
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

s.compile()
