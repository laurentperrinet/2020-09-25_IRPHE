#/usr/bin/env python3
# -*- coding: utf-8 -*-
import os
import markdown
import base64
class Slides:
    """
    TODO: make a class for one slide with labels etc - compile at the end
    TODO: a slide show is a (possibly nested) list of slides

    """
    def __init__(self, meta):
        self.meta = meta
        # Simply using https://docs.python.org/3.3/library/string.html#format-string-syntax to format strings...
        self.header ="""<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8"/>
<meta http-equiv="X-UA-Compatible" content="chrome=1" >

<meta name="description" content="{title}">
<meta name="author" content="{author}">

<meta name="apple-mobile-web-app-capable" content="yes" >
<meta name="apple-mobile-web-app-status-bar-style" content="black-translucent">

<title>{short_title} - {conference}</title>


<!-- General and theme style sheets -->
<link rel="stylesheet" href="{reveal_path}css/reveal.css">
<link rel="stylesheet" href="{reveal_path}css/theme/{theme}.css" id="theme">
    <!-- Code syntax highlighting -->
    <link rel="stylesheet" href="{reveal_path}lib/css/zenburn.css">

        """.format(**meta)

        self.header += """


    <!-- Printing and PDF exports -->
    <script>
            var link = document.createElement( 'link' );
            link.rel = 'stylesheet';
            link.type = 'text/css';
            link.href = window.location.search.match( /print-pdf/gi ) ? 'css/print/pdf.css' : 'css/print/paper.css';
            document.getElementsByTagName( 'head' )[0].appendChild( link );
    </script>


    <!--[if lt IE 9]>
    <script src="{reveal_path}lib/js/html5shiv.js"></script>
    <![endif]-->

    <!-- Loading the mathjax macro -->
    <!-- Load mathjax -->
        <script src="https://cdn.mathjax.org/mathjax/latest/MathJax.js?config=TeX-AMS_HTML"></script>
        <!-- MathJax configuration -->
        <script type="text/x-mathjax-config">
        MathJax.Hub.Config({
            //TeX: { equationNumbers: { autoNumber: "AMS" } },
             tex2jax: {
                inlineMath: [['$','$']],
                displayMath: [['$$','$$']],
                //processEscapes: false,
                processEnvironments: true
            },
            // Center justify equations in code and markdown cells. Elsewhere
            // we use CSS to left justify single line equations in code cells.
            displayAlign: 'center',
            //"HTML-CSS": {
            //    styles: {'.MathJax_Display': {"margin": 0}},
            //    linebreaks: { automatic: true },
            //    availableFonts: ["TeX"]
            //    }
            //}
        });
        </script>
        <!-- End of mathjax configuration -->

        <!-- Get Font-awesome from cdn -->
        <!-- <link rel="stylesheet" href="http://netdna.bootstrapcdn.com/font-awesome/4.1.0/css/font-awesome.css"> -->
</head>

<body>
    <div class="reveal">
        <div class="slides">
        """

        self.footer ="""
        </div>
    </div>

    <script src="{reveal_path}lib/js/head.min.js"></script>
    <script src="{reveal_path}js/reveal.js"></script>

        """.format(**meta)
        self.footer +="""
	<script>

            // Full list of configuration options available at:
            // https://github.com/hakimel/reveal.js#configuration
            Reveal.initialize({

        """
        self.footer +="""
                // The "normal" size of the presentation, aspect ratio will be preserved
                // when the presentation is scaled to fit different resolutions. Can be
                // specified using percentage units.
                width: {width},
                height: {height},

                // Factor of the display size that should remain empty around the content
                margin: {margin},
        """.format(**meta)
        self.footer +="""


                // Display a presentation progress bar
                progress: true,
                slideNumber: 'c/t',

                // Push each slide change to the browser history
                //history: false,

                // Vertical centering of slides
                center: true,

                // Enables touch navigation on devices with touch input
                touch: true,

                // Bounds for smallest/largest possible scale to apply to content
                // minScale: 0.2,
                // maxScale: 1.5,

                // Display controls in the bottom right corner
                controls: false,

                // Enable keyboard shortcuts for navigation
                keyboard: true,

                // Enable the slide overview mode
                overview: true,

                // Loop the presentation
                //loop: false,

                // Change the presentation direction to be RTL
                //rtl: false,

                // Number of milliseconds between automatically proceeding to the
                // next slide, disabled when set to 0, this value can be overwritten
                // by using a data-autoslide attribute on your slides
                //autoSlide: 0,

                // Enable slide navigation via mouse wheel
                //mouseWheel: false,

                // Parallax background image
                //parallaxBackgroundImage: '/Users/laurentperrinet/cloud_nas/2015_RTC/2014-04-17_HDR/figures/p4100011.jpg', // e.g. "https://s3.amazonaws.com/hakim-static/reveal-js/reveal-parallax-1.jpg"

                // Parallax background size
                //parallaxBackgroundSize: '3200px 2000px', // CSS syntax, e.g. "2100px 900px" - currently only pixels are supported (don't use % or auto)

                // This slide transition gives best results:
                transition: 'fade', // default/cube/page/concave/zoom/linear/fade/none

                // Transition speed
                transitionSpeed: 'slow', // default/fast/slow

                // Transition style for full page backgrounds
                backgroundTransition: 'none', // default/linear/none

			    // Turns fragments on and off globally
                fragments: true,

                // Theme
                theme: 'black', // available themes are in /css/theme

        """
        if self.meta['draft']:
            self.footer +="""
                // Notes are only visible to the speaker inside of the speaker view. If you wish to share your notes with others you can initialize reveal.js with the showNotes config value set to true. Notes will appear along the bottom of the presentations.
                showNotes: 'true',
        """
        self.footer +="""
                math: {{
                    mathjax: 'https://cdn.mathjax.org/mathjax/latest/MathJax.js',
                    config: 'TeX-AMS_HTML-full'  // See http://docs.mathjax.org/en/latest/config-files.html
                }},

                // Optional reveal.js plugins
                dependencies: [
                        {{ src: '{reveal_path}lib/js/classList.js', condition: function() {{ return !document.body.classList; }} }},
                        {{ src: '{reveal_path}plugin/markdown/marked.js', condition: function() {{ return !!document.querySelector( '[data-markdown]' ); }} }},
                        {{ src: '{reveal_path}plugin/markdown/markdown.js', condition: function() {{ return !!document.querySelector( '[data-markdown]' ); }} }},
                        {{ src: '{reveal_path}plugin/highlight/highlight.js', async: true, callback: function() {{ hljs.initHighlightingOnLoad(); }} }},
                        {{ src: '{reveal_path}plugin/zoom-js/zoom.js', async: true }},
                        {{ src: '{reveal_path}plugin/notes/notes.js', async: true }},
                        {{ src: '{reveal_path}plugin/math/math.js', async: true }}
        """.format(reveal_path=self.meta['reveal_path'])#.replace('file://', ''))
        self.footer +="""
                ]
        });
        </script>
    </body>
</html>
        """

        self.body = ''

    def open_section(self):
        self.body +=  "<section>"

    def hide_slide(self, image_fname=None, video_fname=None, content='', notes=''):
        """
        do nothing
        """
    def add_slide(self, image_fname=None, video_fname=None, content='', notes='', md=False, embed=None):

        if not image_fname is None:
            if (embed is None and self.meta['embed']) or ((not embed is None ) and embed):
                data_uri = base64.b64encode(open(image_fname, 'rb').read()).decode('utf-8').replace('\n', '')
                image_fname = 'data:image/{ext};base64,{data_uri}'.format(ext=image_fname[-3:], data_uri=data_uri)
            slide = '<section data-background="{}"> '.format(image_fname)
        elif not video_fname is None:
            slide = '<section data-background-video="{}">'.format(video_fname)
        elif md:
            slide = """
<section data-markdown>
<script type="text/template">
        """
        else:
            slide = "<section>"


        slide += content

        slide +="""
            <aside class="notes">
             {}
            </aside>
            """.format(markdown.markdown(notes))

        if md:
            slide += """
</script>
            """

        slide += """
</section>
        """
        self.body += slide

    def add_slide_outline(self, i=None, title='Outline', notes=''):
        content = self.content_title(title)  + '\n<ol>\n'
        for i_, section in enumerate(self.meta['sections']):
            if i_ is i:
                content += """
                    <h3>
                    <li>
                    <p class="fragment highlight-red">
                    {}
                    </p>
                    </li>
                    </h3>
                    """.format(section)
            else:
                content += """
                    <h3>
                    <li>
                    {}
                    </li>
                    </h3>
                    """.format(section)
        content += """
                     </ol>
                    """
        self.add_slide(content=content, notes=notes)

    def add_slide_summary(self, list_of_points, title='Interim summary', notes=''):
        content = self.content_title(title) + """
            <ul>
            """
        for point in list_of_points:
#                        <p class="fragment grow"><li> {} </li></p>
            content += """
                    <h3>
                        <li> {} </li>
                    </h3>
                        """.format(point)
        content += """
                     </ul>
                    """
        self.add_slide(content=content, notes=notes)

    def content_title(self, title):
        if title is None:
            return ''
        else:
            return "<h3>{}</h3>".format(title)

    def content_figures(self, list_of_figures, transpose=False, list_of_weights=None, title=None, height=None, embed=None, fragment=False, bgcolor="black", cell_bgcolor="white"):
        content =  self.content_title(title)
        if fragment:
            fragment_begin = '<p class="fragment">'
            fragment_end = '</p>'
        else:
            fragment_begin, fragment_end = '<p>', '</p>'
        if height is None:
            height = self.meta['height']
        content += """
        <div align="center">
            <table border="0" VALIGN="center" bgcolor={bgcolor} height={height} />
            """.format(bgcolor=bgcolor, height=height)
        n_fig = len(list_of_figures)

        if not transpose:
            if list_of_weights is None:
                widths = [str(int(100/n_fig))+"%" for _ in list_of_figures]
            else:
                total_weight = sum(list_of_weights)
                widths = [str(int(100/n_fig*weight/total_weight))+"%" for weight in list_of_weights]
            content += """
            <tr style="vertical-align:middle">
            """
            for width, fname in zip(widths, list_of_figures):
                if (embed is None and self.meta['embed']) or ((not embed is None ) and embed):

                    data_uri = base64.b64encode(open(fname, 'rb').read()).decode('utf-8').replace('\n', '')
                    fname = 'data:image/{ext};base64,{data_uri}'.format(ext=fname[-3:], data_uri=data_uri)

                if height is None:
                    content += """
                <td width="{width}" style="text-align:center; vertical-align:middle" bgcolor="{cell_bgcolor}" />
                {fragment_begin}
                    <img data-src="{fname}" style="width: 100%" />
                {fragment_end}
                </td>
                """.format(cell_bgcolor=cell_bgcolor, width=width, fname=fname, fragment_begin=fragment_begin, fragment_end=fragment_end)
                else:
                    content += """
                <td height={height} width="{width}" style="text-align:center; vertical-align:middle" bgcolor="{cell_bgcolor}" />
                {fragment_begin}
                    <img data-src="{fname}"  height={height} />
                {fragment_end}
                </td>
                """.format(cell_bgcolor=cell_bgcolor, height=int(height), width=width, fname=fname, fragment_begin=fragment_begin, fragment_end=fragment_end)
            content += """
                        </tr>
                        """
        else: # TODO make more pythonic...

            if list_of_weights is None:
                heights = [str(int(height/n_fig)) for _ in list_of_figures]
            else:
                total_weight = sum(list_of_weights)
                heights = [str(int(height/n_fig*weight/total_weight)) for weight in list_of_weights]
            for height_, fname in zip(heights, list_of_figures):
                if (embed is None and self.meta['embed']) or ((not embed is None ) and embed):
                    data_uri = base64.b64encode(open(fname, 'rb').read()).decode('utf-8').replace('\n', '')
                    fname = 'data:image/{ext};base64,{data_uri}'.format(ext=fname[-3:], data_uri=data_uri)
                content += """
                <tr style="vertical-align:middle">
                    <td width="100%" style="text-align:center; vertical-align:middle" bgcolor="{cell_bgcolor}" />
                    {fragment_begin}
                        <img data-src="{fname}" height={height_} />
                    {fragment_end}
                    </td>
                </tr>
                """.format(cell_bgcolor=cell_bgcolor, height_=height_, fname=fname,
                        fragment_begin=fragment_begin, fragment_end=fragment_end)
        content += """
                        </table>
                        </div>
                        """
        return content
    def content_bib(self, author, year, journal):
        return """
        <div style="text-align:right;">{author} ({year}) <em>{journal}</em>  </div>
        """.format(author=author, year=year, journal=journal)
        return content

    def close_section(self):
        self.body +=  "\n</section>\n"

    def compile(self, filename='index.html'):
        html = self.header + self.body + self.footer
        with open(filename, 'w') as f: f.write(html)
# s.body += """
# <script>
#       document.getElementById('theme').setAttribute('href','css/theme/white.css'); return false;">
# </script>
