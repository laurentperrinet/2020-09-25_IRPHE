#! /usr/bin/env python3
# -*- coding: utf-8 -*-
from slides import Slides
import os
__author__ = "Laurent Perrinet INT - CNRS"
__licence__ = 'BSD licence'
DEBUG = True
DEBUG = False
"""

Documentation for slides.py - serves as a template for future presentations.


"""

home = os.environ['HOME']


meta = dict(
    embed=True,
    draft=DEBUG,  # show notes etc
    width=1600,
    height=1000,
    margin=0.1618,
    # reveal_path='https://cdnjs.cloudflare.com/ajax/libs/reveal.js/3.7.0/',
    reveal_path='https://cdn.jsdelivr.net/npm/reveal.js@3.8.0/',
    #reveal_path='https://rajgoel.github.io/reveal.js/',
    #reveal_path = 'https://s3.amazonaws.com/hakim-static/reveal-js',
    theme='night',

    author='Laurent U Perrinet, INT',
    author_link='<a href="http://invibe.net">Laurent U Perrinet, INT</a>',
    title="""A simple way to make slideshows?""",
    short_title="What's slides.py?",
    conference="Example conference",
    Acknowledgements="""<h3>Acknowledgements:</h3>
            <ul><li> Hakim El Hattab for <a href="http://lab.hakim.se/reveal-js">reveal-js</a>
                <li>Some people...</li>
                <li>Lots more people...</li>
           </ul>

""",
    sections=['Intro', 'Methods', 'Results']
)
s = Slides(meta)
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

###############################################################################
# Intro - 5''
###############################################################################
###############################################################################
intro = """
<h2 class="title">{title}</h2>
<h3>{author_link}</h3>
""".format(**meta)
intro += s.content_figures(
    [os.path.join(figpath, "troislogos.png")], bgcolor="black",
    height=s.meta['height']*.3, width=s.meta['height']*1.2)
intro += """
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
###############################################################################
# Methods - 15''
###############################################################################
###############################################################################
s.open_section()
s.add_slide_outline(1)
s.add_slide_summary(
    ['Go fullscreen using the ``f`` key',
     'You can have an overlook using the ``o`` key',
     'Navigate using the arrow keys',
     'see notes using the ``n`` key'],
    notes="""
* and write notes using markdown

""")
s.close_section()
###############################################################################
# Results - 15''
###############################################################################
###############################################################################
s.open_section()
s.add_slide_outline(2)

s.add_slide(content=s.content_figures(
    [os.path.join(figpath, "troislogos.png")], bgcolor="black",
    height=s.meta['height']*.3, width=s.meta['height']*1.2),
            notes="""
You can embed images.
""")

s.add_slide(content="""
    <video controls autoplay loop width=60%/>
      <source type="video/mp4" src="{}">
    </video>
    """.format(s.embed_video(os.path.join(figpath, 'video.mp4'))),
            notes="""
You can also embed videos.
""")


myurl = 'https://docs.python.org/3/_static/py.png'
myurl = "https://upload.wikimedia.org/wikipedia/commons/thumb/2/20/Gruenebaumpython4cele4.jpg/1200px-Gruenebaumpython4cele4.jpg"
s.add_slide(content=s.content_figures(
                    [myurl], bgcolor="black",
                    height=s.meta['height']*.3, width=s.meta['height']*1.2),
            notes="""
You can embed images from an URL.
""")

s.close_section()
###############################################################################
# Conclusion - 15''
###############################################################################
###############################################################################
s.open_section()
s.add_slide_outline()
s.add_slide_summary(
    ['install using instructions on <a href=https://github.com/laurentperrinet/slides.py>https://github.com/laurentperrinet/slides.py</a>',
     'suggest <a href="https://github.com/laurentperrinet/slides.py/issues">improvments or issues</a>, ',
     'fork!'],
    notes="""
* and write notes using markdown

""")
s.add_slide(content=intro,
            notes="""
Thanks for you attention!
""")
s.close_section()

###############################################################################
s.compile(filename='docs/index.html')
