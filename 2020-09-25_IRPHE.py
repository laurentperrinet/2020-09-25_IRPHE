#!/usr/local/bin/python
# coding: latin-1
__author__ = "Laurent Perrinet INT - CNRS"
__licence__ = 'GPL licence'
DEBUG = True
DEBUG = False
"""
2020-09-25_IRPHE
"""

fig_width = 12

import os
# https://docs.python.org/3.8/library/pathlib.html
# import pathlib
from pathlib import Path

home = Path(os.environ['HOME'])

# figpath_talk = Path.cwd().joinpath('figures')
figpath_talk = 'figures'
Path.cwd().joinpath(figpath_talk).mkdir(parents=True, exist_ok=True)

# print(figpath_talk)
# figpath_slides = os.path.join(home, 'quantic/libraries/slides.py/figures/')
figpath_slides = 'https://laurentperrinet.github.io/slides.py/figures/'
#
import sys
print(sys.argv)
tag = sys.argv[0].split('.')[0]
if len(sys.argv) > 1:
    slides_filename = sys.argv[1]
else:
    slides_filename = None

from academic.cli import slugify
slugified = slugify(tag)

print('😎 Welcome to the script generating the slides for ', tag)
try:
    YYYY = int(tag[:4])
    MM = int(tag[5:7])
    DD = int(tag[8:10])
except:
    from datetime import datetime
    DD = datetime.now().day
    MM = datetime.now().month
    YYYY = datetime.now().year

# see https://github.com/laurentperrinet/slides.py
from slides import Slides

height_ratio = .9
sections = ['*Natural* Vision', 'Deep Learning', 'Predictive processes', 'Perspectives']

meta = dict(
 embed=False,
 draft=DEBUG,  # show notes etc
 width=1600,
 height=1000,
 margin=0.15,
 reveal_path='https://laurentperrinet.github.io/2020-09-14_IWAI/reveal.js-master/',
 theme='simple',
 bgcolor="white",
 author='Perrinet, Laurent U',
 author_link=f'<a href="https://laurentperrinet.github.io/talk/{slugify(tag)}/">Laurent Perrinet</a>',
 title="Understanding natural vision <BR> using deep predictive coding",
 short_title="Understanding natural vision using deep predictive coding",
 conference="Séminaire à l'Institut de Recherche sur les Phénomènes Hors Équilibre",
 conference_url='https://laurentperrinet.github.io/talk/2020-09-25-irphe',
 short_conference=' (IRPHÉ)',
 location='Marseille (France)',
 abstract="""Building models which efficiently process images is a great source of inspiration to better understand the processes which underly our visual perception. I will present some classical models stemming from the Machine Learning community and propose some extensions inspired by Nature. For instance, Sparse Coding (SC) is one of the most successful frameworks to model neural computations at the local scale in the visual cortex. It directly derives from the efficient coding hypothesis and could be thought of as a competitive mechanism that describes visual stimulus using the activity of a small fraction of neurons. At the structural scale of the ventral visual pathways, feedforward models of vision (CNNs in the terminology  of deep learning) take into account neurophysiological observations and provide as of today the most successful framework for object recognition tasks. Nevertheless, these models do not leverage the high density of feedback and lateral interactions observed in the visual cortex. In particular, these connections are known to integrate contextual and attentional modulations to feedforward signals. The Predictive Coding (PC) theory has been proposed to model top-down and bottom-up interaction between cortical regions. We will here introduce a model combining Sparse Coding and Predictive Coding in a hierarchical and convolutional architecture. Our model, called Sparse Deep Predictive Coding (SDPC), was trained on several different databases including faces and natural images. We analyze the SPDC from a computational and a biological perspective and we combine neuroscientific evidence with machine learning methods to analyze the impact of recurrent processing at both the neural organization and representational levels. These results from the SDPC model additionally demonstrate that neuro-inspiration might be the right methodology to design more powerful and more robust computer vision algorithms.""",
 YYYY=YYYY, MM=MM, DD=DD,
 tag=tag,
 projects='aprovis-3-d',
 time_start='15:45:00',
 time_end='16:30:00',
 url=f'https://laurentperrinet.github.io/talk/{slugify(tag)}',
 sections=sections
)

###############################################################################
# 🏄🏄🏄🏄🏄🏄🏄🏄            QR CODE                      🏄🏄🏄🏄🏄🏄🏄🏄
###############################################################################

# https://pythonhosted.org/PyQRCode/rendering.html
# pip3 install pyqrcode
# pip3 install pypng

# figname_qr = Path.cwd().joinpath(figpath_talk).joinpath('qr.png')
figname_qr = os.path.join(figpath_talk, 'qr.png')
if DEBUG or (not Path(figname_qr).is_file()):
    import pyqrcode as pq
    code = pq.create(meta['url'])
    code.png(figname_qr, scale=5)

print(meta['sections'])
s = Slides(meta)

###############################################################################
# 🏄🏄🏄🏄🏄🏄🏄🏄                INTRO                    🏄🏄🏄🏄🏄🏄🏄🏄
###############################################################################
height_px = 120
# path_people = os.path.join(home, 'ownCNRS/2019-01_LACONEU/people')
path_people = home.joinpath('github/hugo_academic/content/authors')
# path_people = 'https://laurentperrinet.github.io/authors/'
# ls ~/github/hugo_academic/content/authors/**/avat*
People = ''
# People += s.content_imagelet(path_people.joinpath('chloe-pasturel/avatar.png'), height_px, embed=True)
People += s.content_imagelet(path_people.joinpath('hugo-ladret/avatar.jpg'), height_px, embed=True)
# People += s.content_imagelet(path_people.joinpath('james-a-bednar/avatar.jpg'), height_px, embed=True)
# People += s.content_imagelet(path_people.joinpath('jens-kremkow/avatar.jpg'), height_px, embed=True)
# People += s.content_imagelet(path_people.joinpath('karl-friston/avatar.jpg'), height_px, embed=True)
# People += s.content_imagelet(path_people.joinpath('kiana-mansour-pour/avatar.jpg'), height_px, embed=True)
# People += s.content_imagelet(path_people.joinpath('laurent-u-perrinet/avatar.jpg'), height_px, embed=True)
# People += s.content_imagelet(path_people.joinpath('manuel-samuelides/avatar.jpg'), height_px, embed=True)
# People += s.content_imagelet(path_people.joinpath('maria-jose-escobar/avatar.jpg'), height_px, embed=True)
# People += s.content_imagelet(path_people.joinpath('mina-a-khoei/avatar.jpg'), height_px, embed=True)
# People += s.content_imagelet(path_people.joinpath('nicole-voges/avatar.gif'), height_px, embed=True)
# People += s.content_imagelet(path_people.joinpath('paula-s-leon/avatar.jpg'), height_px, embed=True)
# People += s.content_imagelet(path_people.joinpath('simon-j-thorpe/avatar.jpg'), height_px, embed=True)
People += s.content_imagelet(path_people.joinpath('victor-boutin/avatar.jpg'), height_px, embed=True)
# People += s.content_imagelet(path_people.joinpath('wahiba-taouali/avatar.jpg'), height_px, embed=True)
# People += s.content_imagelet(path_people.joinpath('yves-fregnac/avatar.jpg'), height_px, embed=True)
# People += s.content_imagelet(path_people.joinpath('rick-a-adams/avatar.jpg'), height_px, embed=True)
# People += s.content_imagelet(path_people.joinpath('anna-montagnini/avatar.jpg'), height_px, embed=True)
# People += s.content_imagelet(path_people.joinpath('laurent-madelain/avatar.png'), height_px, embed=True)
# People += s.content_imagelet(path_people.joinpath('jean-bernard-damasse/avatar.jpg'), height_px, embed=True)
# People += s.content_imagelet(path_people.joinpath('stephane-viollet/avatar.jpg'), height_px, embed=True)
People += s.content_imagelet(path_people.joinpath('alberto-vergani/avatar.jpg'), height_px, embed=True)
People += s.content_imagelet(path_people.joinpath('angelo-franciosini/avatar.jpg'), height_px, embed=True)
People += s.content_imagelet(path_people.joinpath('frederic-y-chavane/avatar.png'), height_px, embed=True)
People += s.content_imagelet(path_people.joinpath('emmanuel-dauce/avatar.jpg'), height_px, embed=True)
People += s.content_imagelet(path_people.joinpath('etienne-rey/avatar.jpg'), height_px, embed=True)


s.meta['Acknowledgements'] = f"""
{People}
"""
# s.meta['Acknowledgements'] = f"""
# <small>
# <h5>Acknowledgements:</h5>
# <ul><li> Hakim El Hattab for <a href="https://revealjs.com/">reveal-js</a>
# <li>Some people...</li>
# <li>Lots more people...</li>
# </ul>
# <BR>
# {People}</a>
# <BR>
#     This work was supported by ....
# </small>
#
# """
s.open_section()
###############################################################################
intro = """
<h2 class="title">{title}</h2>
<h3>{author_link}</h3>
""".format(**meta)
# intro += s.content_imagelet('figures/ins-logo.png',
#                             s.meta['height']*.24,
#                             embed=False)
intro += s.content_imagelet('https://laurentperrinet.github.io/slides.py/figures/troislogos.png',
                            s.meta['height']*.32,
                            embed=False)  # bgcolor="black",
intro += """
<h4><a href="{conference_url}">{conference}{short_conference}</a> {DD}/{MM}/{YYYY} </h4>

{Acknowledgements}
""".format(**meta)
###############################################################################
###############################################################################
###############################################################################
###############################################################################
###############################################################################
###############################################################################
###############################################################################
###############################################################################
###############################################################################

s.add_slide(content=intro,
            notes="""
1

Bonjour je suis Laurent Perrinet et je vais vous parler aujourd’hui de la vision naturelle. Je vais essayer de vous démontrer l’importance que son étude peut avoir sur la construction d’algorithmes de vision par ordinateur mais aussi pour nous mettre permettre d’avoir une meilleure compréhension des principes neuronaux qui sous-tendent le fonctionnement de notre cerveau.

La vision est ce processus qui nous permet de faire sens à partir du monde lumineux qui nous entoure. Je vous remercie de m'avoir invité, car son étude pourrait a priori par être éloigné du domaine de recherche qui sont étudiés à votre institut ... et je vais essayer de démontrer durant cet exposé que la déraisonnable efficacité de la vision dans le monde naturel peuvent se comprendre comme des mécanismes d’intégration dynamique qui ne vous seront sûrement pas étranges... On pourra donc espérer faire des ponts entre ces différents domaines d’études.

""")
s.close_section()
###############################################################################
# 🏄🏄🏄🏄🏄🏄🏄🏄 Vision 🏄🏄🏄🏄🏄🏄🏄🏄
###############################################################################
i_section = 0
###############################################################################
s.open_section()
s.add_slide_outline(i_section,
            notes="""2

            Durant cet exposé, je vais présenter quelques principes fondamentaux, puis aussi présenter les techniques récentes développées dans le cadre de l’apprentissage profond. Enfin, je vais présenter nos travaux sur les modèles de processus productif pour la vision et proposer des perspectives de recherche.""")

for layer in ['brain', 'pathways', 'ventral']:
    s.add_slide(content=s.content_figures(
                [os.path.join(figpath_talk, f"architecture_vision_{layer}.svg")],
                height=s.meta['height']*height_ratio),
                notes="""

3

Commençons par le début et par l’anatomie du système visuel. Cette figure montre une représentation schématique du cerveau chez l’homme et en particulier le tronc cérébral, le cervelet et le neocortex.

4

De façon schématique on peut décrire l'anatomie de la vision comme suivant des chemins depuis l’oeil, via le thalamus, pour converger sur l'aire corticale primaire de la vision (AKA V1). Depuis cette aire cérébrale, l’information est ensuite multiplexée entre une voie ventrale et une voie dorsale. La voie dorsale analyse préférentiellement la temporalité de l’information visuelle, comme par exemple le mouvement dans une image. Elle est donc essentielle par exemple pour guider les mouvement des yeux notamment quand ils servent à compenser le mouvement d'un objet visuel.

5

La voie ventrale est principalement impliqué dans la reconnaissance des formes comme par exemple la catégorisation des images visuelles. Ce processus peut lui-même être décomposé en une séquence de différentes étapes de traitement de l’information depuis la rétine et le thalamus, pour passer dans les aires visuelles primaires V1, V2, V3 jusqu’au aires corticales située dans le lobe inferotemporal. Ainsi certaines neurones de ces aires peuvent être sensible à des caractéristiques visuelle très particulières comme par exemple des objets ou des visages, et ceci indépendamment de leur position dans l’espace visuel. Cette organisation ressemble grossièrement aux chaînes de traitement de l’information que l’on rencontre dans les algorithmes de vision par ordinateur, depuis l'entrée rétinienne jusqu’à une sortie, par exemple motrice. Il est toutefois remarquable de noter que la vision nous paraît comme un mécanisme tout à fait naturel, et que le monde visuel me paraissent tout à fait stable alors que ce système est soumis à des contraintes majeures.
                """)

# author, year, journal, title='', url=None
bib = s.content_bib("LP", "2019", "Illusions et hallucinations visuelles : une porte sur la perception ", url="https://theconversation.com/illusions-et-hallucinations-visuelles-une-porte-sur-la-perception-117389")

for url in ['https://laurentperrinet.github.io/2020-09-14_IWAI/figures/CNS-general-II-A.png',
            'https://images.theconversation.com/files/277070/original/file-20190529-192383-zy01r.jpg']:
    fig = s.content_figures([url], bgcolor="black", height=s.meta['height']*height_ratio)

    s.add_slide(content=fig + bib,
                notes="""
6

Il faut tout d’abord noter que dès la rétine, l’information visuelle (ici chez l’homme) est fortement focalisée. En effet la majorité de l’information est concentrée sur la macula, qui est la région autour de l’axe optique. Par l’anatomie de l’œil que l’on voit sur cette figure  et qui correspond à la majorité des "pixels", c’est-à-dire des photos récepteurs placé sur le fond de l’œil et qui constitue le senseur sur la rétine. Schématiquement on peut illustrer cette transformation sur une image classique en A, jusqu’à sa transformation dans une carte de type log-polaire de telle sorte qu’on peut comprimer l’image en une représentation en C, et que l’on peut aussi représenter dans l’espace visuel sous la forme de la figure D. Cette transformation de l’espace visuel induit une forte distorsion de l’image qui est difficilement imaginable, et des illusions d’optique permet de le révéler. Un exemple sont les illusions qui mettent en évidence la tache aveugle c’est-à-dire le point où la sortie de la rétine converge sur  le nerf optique et qui n'est pas photosensible. Certaines illusions utilisent des configurations pour lesquelles cette distorsion induit une certaine instabilité…

7

Un exemple cette illusion dit-il dites dites des serpents qui tournoient. Cette illusion crée par le professeur Akiyoshi Kitaoka induit des hallucinations de mouvements dans une image qui n’en contient pas. Bien que l’image soit totalement statique, l’interférence des patterns concentriques interfèrent avec la géométrie de la rétine. Cela induit des illusions de mouvement et de façon globale la stabilité de la figure géométrique...
                """)

# author, year, journal, title='', url=None
bib = s.content_bib("LP", "2020", "Temps et cerveau : comment notre perception nous fait voyager dans le temps", url="https://theconversation.com/temps-et-cerveau-comment-notre-perception-nous-fait-voyager-dans-le-temps-127567")

for url in ['https://laurentperrinet.github.io/2019-04-18_JNLF/figures/scheme_thorpe.jpg',
            'https://laurentperrinet.github.io/2019-04-18_JNLF/figures/figure-tsonga.png',
            'https://upload.wikimedia.org/wikipedia/commons/6/60/Flash_lag.gif',
            ]:
    fig = s.content_figures([url], bgcolor="black", height=s.meta['height']*height_ratio)

    s.add_slide(content=fig + bib, notes="""

8

Une autre contrainte auxquelles notre cerveau est confronté et le fait que l’information visuelle mette un certain temps pour passer d’un coté à l’autre le long des voies visuelles. Je reproduis ici une figure établie par Simon Thorpe qui montre chez le macaque les différentes latence de l’information visuelle quand elle voyage depuis la rétine jusqu’à une réponse motrice. Ainsi si une image est présentée au temps zéro elle sortira de la rétine après environ 30 millisecondes, puis sera traité dans l’ère visuelle primaire après 50 millisecondes pour être traité le long de la voie ventrale en 100 millisecondes. Cette information pourra ensuite être traitée pour atteindre les aires motrices pour établir une commande motrice et enfin une réponse en environ 200 ms. C’est l'ordre de grandeur du temps qu’il faut pour répondre à une image et qui est observé aussi chez les humains. Je vais maintenant vous illustrer les conséquences de ses délais neuronaux.

9

En effet si l’on considère une situation relativement naturel relevant du domaine de la vision c’est-à-dire ici Jau Wilfried son gars son gars à vous le donne en train en train d’essayer de rattraper passer une chatte est une chatte est un chat pour une vitesse pour une balle se déplaçant à une vitesse d’environ 20 m/s.
En rapportant les délais neuronaux par rapport à la balle à l’instant présent telle qu’elle est au centre de l’image, On n’en déduit que l’image qui est vu par le cerveau dans l’air visuel primaire dans les airs de reconnaissance le long de la voie dorsale par exemple et décaler dans le temps de s’ennuyer souvent et donc dans l’espace d’environ 1 m.
De la même façon, la position de la balle la position de la balle par rapport à une action possible prise à ce moment-là c’est-à-dire à l’instant présent doit être effectué pour une position de Laval telle qu’elle sera 80 000 secondes après le temps présent c’est-à-dire en avant d’une distance équivalente à à peu près 80 cm.
Devant l’urgence de pouvoir répondre de façon efficace à une telle scène, on comprend que le système visuel a été optimisé durant les millions d’années de la sélection de l’éternel. Pour permettre de réagir efficacement à ce genre de situation.
Ce genre d’optimisation de la vision des processus de la vision peut être mis en évidence dans une illusion extrême moment simple dite du flash retardé.


10

Dans cette illusion, la consigne est de fixer le point vert au centre de l’écran. Si maintenant je vous demande de me donner la position du point rouge au moment où le point vert apparaît, vous me direz sans doute il apparaît légèrement à droite de celui ci.
Pourtant, à l’instant où le point vert apparaît, le point rouge est exactement à la verticale du point vert. Ceci est dû au fait que le point vert apparaît de façon non prédictive alors que le point rouge, qui suit qui suit une trajectoire rectiligne et continue, est lui représenté par le système visuel en avant de sa trajectoire. Cela implique aussi le système visuel ne regarde pas de façon passive l’information rétinienne mais plutôt qu’il perçoit une information telle qu'elle est transformée par les processus visuels. On voit pas ce qu’on voit mais on voit ce qu’on croit.

Par conséquent, on a pu mettre en évidence par ces simples expériences la déraisonnable efficacité du système visuel.

    """)

s.close_section()
###############################################################################
# 🏄🏄🏄🏄🏄🏄🏄🏄       Deep Learning  - 15''              🏄🏄🏄🏄🏄🏄🏄🏄
###############################################################################
i_section = 1
###############################################################################
s.open_section()
s.add_slide_outline(i_section,
notes="""

11

Examinons maintenant l’état de l'art de nos connaissances en vision par ordinateur et en particulier des progrès récents effectués en apprentissage profond.

""")

# author, year, journal, title='', url=None
bib = s.content_bib("Matthew Ricci and Thomas Serre", "2020", "Hierarchical Models of the Visual System", url="https://link.springer.com/referenceworkentry/10.1007%2F978-1-4614-7320-6_345-2")

for layer in ['ventral', 'cnn']:
    s.add_slide(content=s.content_figures(
                [os.path.join(figpath_talk, f"architecture_vision_{layer}.svg")],
                height=s.meta['height']*height_ratio) + bib,
                notes="""

12

On a vu tout à l’heure que l’anatomie du système visuel dessine,  en ce qui concerne la reconnaissance d’image, une chaîne de traitement de l’information le long de la voie ventrale.

13

Une telle architecture est largement utilisée dans des modèles hiérarchique du système visuel comme décrit à dans cette revue qui va transformer une image d’entrée à travers différentes couches prototypiques de traitement, jusqu’à une représentation progressivement plus abstraite jusqu’à obtenir une reconnaissance sous forme sémantique.

                """)


fig = s.content_figures(
            [os.path.join(figpath_talk, f"Serre_Fig{i}_DL.png") for i in ['3', '4']],
            height=s.meta['height']*height_ratio, fragment=True)

s.add_slide(content=fig + bib, notes="""

14
Ce type d’architecture consiste à décomposer les niveaux d’analyse en des processus  traitant progressivement des caractéristiques visuelles du particulier au général.
Dans la première couche (V1), nous avons un traitement qui va extraire les contours de l’image pour ensuite analyser les courbure de ces différents contours, pour ensuite introduire des représentations plus complexes et abstraites et enfin obtenir des unités de classification ("un renard"). Mathématiquement, on peut formaliser ce type de modèle sous la forme d’un réseau de neurones convolutionnel et qui constitue la base de la grande majorité des algorithmes d’apprentissage profond qui sont utilisés de nos jours.
L’opération de base correspond à un filtrage linéaire qui utilise un noyau conditionnel et qui va représenter la corrélation de ce noyau avec des sous partie de l’image. Cette opération est répétée dans une même couche sur différents canaux et va permettre par exemple de représenter sur une même carte les différentes orientations des contours sur cette carte. Avant de propager ce traitement dans une nouvelle couche une étape importante et d’opérer une transformation non linéaire non linéaire qui correspondent à une rectification et à une intégration par exemple en éliminant un neurone sur deux.
On voit ainsi que au fur et à mesure que l’on monte dans la hiérarchie, les champs récepteurs deviennent progressivement de plus en plus grands comme on peut voir ici en comparant les champs récepteur RF1 et RF2.

""")


# author, year, journal, title='', url=None
bib = s.content_bib("Sadek Alaoui", "2017", "Convolutional Neural Network", url="http://sqlml.azurewebsites.net/2017/09/12/convolutional-neural-network/")
fig = s.content_figures([os.path.join(figpath_talk, 'null-38.png')], bgcolor="black", height=s.meta['height']*height_ratio)
s.add_slide(content=fig + bib, notes="""
15

Grâce notamment aux progrès dans les algorithmes d'apprentissage (la retro propagation du gradient), dans le matériel (les GPUs) mais aussi dans l'organisation de la communauté pour obtenir des benchmarks efficaces, ces algorithmes ont rapidement progressé sur une tache complexe de reconnaissance (IamgeNet) jusqu'à atteindre la performance humaine (5%) en 2015. Ce progrès vient au prix d'une explosion de la complexité de ces réseaux, mesurée ici avec le nombre de couches des CNNs.
    """)
# author, year, journal, title='', url=None
bib = s.content_bib("Dario Amodei & Danny Hernandez", "2018", "OpenAI", url="https://openai.com/blog/ai-and-compute/")
fig = s.content_figures([os.path.join(figpath_talk, 'ai-and-compute-all.png')], bgcolor="black", height=s.meta['height']*height_ratio)
s.add_slide(content=fig + bib, notes="""

16

En regardant sur une échelle temporelle plus large, on voit que c'est en tendance suivez la loi de Moor depuis les années 1960 et a clairement explosé depuis l'introduction de l'apprentissage profond… C'est vraiment une nouvelle ère qui vient de s'ouvrir !

    """)


# author, year, journal, title='', url=None
bib = s.content_bib("Thomas Serre", "2019", "Deep Learning: The Good, the Bad, and the Ugly", url="https://www.annualreviews.org/doi/abs/10.1146/annurev-vision-091718-014951")

for url in  [f'https://www.annualreviews.org/na101/home/literatum/publisher/ar/journals/content/vision/2019/vision.2019.5.issue-1/annurev-vision-091718-014951/20190909/images/large/vs50399.f{i}.jpeg' for i in ['3', '4']]:
    fig = s.content_figures([url], bgcolor="black", height=s.meta['height']*height_ratio)

    s.add_slide(content=fig + bib, notes="""

17

En dehors des progrès effectués dans la catégorisation d'images (ce qui est très important pour les entreprises qui financent ces recherche -Facebook, Amazon, ou Google- on a vu l'émergence de nouvelles techniques qui montre toute la créativité de la communauté en apprentissage profond. En suivant cet article de revue de Thomas Serre, je citerai par exemple la capacité de pouvoir faire du transfert de style c'est-à-dire de pouvoir transformer une image dans le style d'un peintre donné. Ou alors la création d'images complètement nouvelles comme par exemple montrer dans le panneau d,  ou alors dans cette peinture dans le panneau B qui a été créé par un algorithme génératif et qui a même atteint un prix mirobolant dans une vente aux enchères....

18

Mais tout n'est pas rose dans le monde de l'apprentissage profond…
En effet, ces modèles qui ont gagné le concours de reconnaissance d'image peuvent être très sensibles à des petites perturbations qui va faire qu'une chaussette va être reconnu comme un éléphant, qu'un panneau de signalisation ne pourra pas être reconnu. si il contient des bouts de sketch de scotch, , qu'une personne va changer d'une entité si elle porte des lunettes. Pire, des algorithmes qui atteignent des niveaux de performance sur-humains seront incapables de généraliser leurs performances si on change le type de perturbation qui est appliquée aux images.
Il existe d'autres faiblesses, comme le manque d'interprétabilité, mais...


    Figure 3  Art and image synthesis with deep neural networks. (a) Style transfer with convolutional neural networks (CNNs). The content of an image (top, first panel) is combined with the style of three distinct paintings (top, second, third, and fourth panels) to synthesize a new artistic image (bottom row) using a neural network (Gatys et al. 2017). Image credit: Matthias Bethge (adapted with permission). (b) The Portrait of Edmond Belamy produced by a generative adversarial network (GAN) and sold by Christie's for $432,500 in October 2018. Reproduced with permission from the copyright holder. Sotheby's Contemporary Art Day Auction held in March 2019 also featured a machine installation that used neural networks to generate an infinite stream of portraits. Mainstream artists including Refik Anadol, Trevor Paglen, and Jason Salavon have started to incorporate neural networks as a part of their artistic process. (c) Latest improvements in style transfer by leveraging attentional mechanism to produce transfers that respect the semantic content of the original image (Park & Lee 2019). Image credit: Dae Y. Park and Kwang H. Lee (adapted with permission). (d) Synthetic images generated by a large generative adversarial network named BigGAN (Brock et al. 2019). Adapted with permission from the authors.

    """)

# TODO : lee sedol
fig = s.content_figures(['https://laurentperrinet.github.io/sciblog/files/2016-07-07_EDP-proba/figures/power.png'], height=s.meta['height']*height_ratio)
s.add_slide(content=fig + bib, notes="""

19

... un des pires aspects est la comparaison avec l'intelligence naturelle. À ce titre le match d'Alpha Go, s'il constitue un milestone dans l'apprentissage par renforcement, constitue aussi une illustration de la grande différence d'énergie déployée dans cet algorithme par rapport au 5W nécessaires pour alimenter un cerveau humain...

""")

s.close_section()
###############################################################################
# 🏄🏄🏄🏄🏄🏄🏄🏄       Predictive processes - 15''        🏄🏄🏄🏄🏄🏄🏄🏄
###############################################################################
i_section = 2
###############################################################################
s.open_section()
s.add_slide_outline(i_section,
notes="""

20

Dans le suite, nous allons essayer d'explorer des alternatives, comme par exemple le codage prédictif.

""")


# author, year, journal, title='', url=None
SDPC_bib = s.content_bib('Boutin, Franciosini, Chavane, Ruffier, LP', '2020', 'submitted',
            url="https://laurentperrinet.github.io/publication/boutin-franciosini-chavane-ruffier-perrinet-20")

bib = s.content_bib("Matthew Ricci and Thomas Serre", "2020", "Hierarchical Models of the Visual System", url="https://link.springer.com/referenceworkentry/10.1007%2F978-1-4614-7320-6_345-2")

# for layer in ['ventral', 'cnn']:
for layer in ['cnn']:
    s.add_slide(content=s.content_figures(
                [os.path.join(figpath_talk, f"architecture_vision_{layer}.svg")],
                height=s.meta['height']*height_ratio) + bib,
                notes="""

21

En effet, nous avons vu que la vision artificielle considère des processus "en avant", mais si l'on zoome sur une partie de l'aire V1 par exemple...

                """)


url_talk = 'https://laurentperrinet.github.io/2019-04-03_a_course_on_vision_and_modelization/figures/'
# author, year, journal, title='', url=None
bib = s.content_bib("Bosking et al.", "1997", "Journal of Neuroscience", url="https://laurentperrinet.github.io/2019-04-03_a_course_on_vision_and_modelization/#/0/4")
fig = s.content_figures([f'{url_talk}Bosking97Fig4.jpg'], bgcolor="black", height=s.meta['height']*height_ratio)
s.add_slide(content=fig + bib, notes="""
22

on découvre alors qu'il existe un riche réseau de connections latérales (dénotées ici comme des points noirs au dessus de la représentation des orientations en couleurs). Des analyses ont montré que ces connections sont largement majoritaires en nombre, de l'ordre de 95% du nombre de boutons synaptiques.
""")

bib = s.content_bib("Bastos et al.", "2012", "Canonical Microcircuits for Predictive Coding", url="http://dx.doi.org/10.1016/j.neuron.2012.10.038")

for figname in ["Canonical_Microcircuit.svg", "Bastos12Fig5.png"]:
    s.add_slide(content=s.content_figures(
            [
                os.path.join(figpath_talk, figname),
                # os.path.join(figpath_talk, "Bastos12Fig5.png"),
            ],
            height=s.meta['height']*height_ratio, fragment=True) + bib,
            notes="""

23

Ces connections participent plus généralement à un circuit prototypique, le micro-circuit cortical, qui intègre à la fois le traitement en avant, que les connections latérales mais aussi les connections en retour qui proviennent d'aires "supérieures"...

24

.. et pourraient être compris comme l'implémentation d'un circuit prédictif qui minimiserait la surprise d'un modèle interne. Le champion de cette modélisation est Karl Friston de l'UCL.

            """)


#
# for suffix in ['_a', '_b', '_c', '']:
#     s.add_slide(content=s.content_figures(
#         [os.path.join(url_talk, 'boutin-franciosini-ruffier-perrinet-19_figure1' + suffix + '.png')], bgcolor="black",
#     title=None, embed=False, height=s.meta['height']*.85)+SDPC_bib,
#            notes="""
#
# figure 1 of SDPC
#
# cf. research/NN-2018
#
# """)

for suffix in ['_FF', '_RNN', '']:
    s.add_slide(content=s.content_figures(
        [os.path.join(figpath_talk, 'BoutinFranciosiniChavaneRuffierPerrinet20' + suffix + '.svg')], bgcolor="black",
    title=None, embed=False, height=s.meta['height']*height_ratio)+SDPC_bib,
           notes="""


25

Basés sur ce genre de principe, nous avons étendu un modèle convolutionnel classique comportant des couches convolutionnelles...

26

... un processus récurrent intra cortical ...

27

Mais aussi des connections ré-entrantes (ici dénotées en bleu). Dans une telle architecture, l'algorithme de retro propagation du gradient n'est plus possible. Nous avons introduit un algorithme d'apprentissage plus réalistes biologiquement car il est 1/local à l'aire corticale et qui s'applique à cette architecture, 2/ totalement auto-supervisé, c'est-à-dire qu'il ne dépend pas d'une tache de catégorisation.

""")

# s.add_slide(content="""
#     <video controls loop width=85%/>
#       <source type="video/mp4" src="{}">
#     </video>
#     """.format(f'{url_talk}training_video_ATT.mp4'),
#     notes="""
#
#     Let's now apply that to natural images of faces
#
# """)
s.add_slide(content="""
    <video controls loop width=85%/>
      <source type="video/mp4" src="{}">
    </video>
    """.format(f'{url_talk}training_video_ATT.mp4')+SDPC_bib,
    notes="""

28

Entrainé sur une base d'image de visage, cet algorithme permet de voir émerger des noyaux de convolution dans la première et la deuxième couche du réseau. Il est remarquable de remarquer, qu'à la différence d'un CNN classique, les noyaux de convolutions sont interprétables et correspondent à des bords (couche 1) mais aussi à de "proto-concepts" comme ces champs récepteurs sensibles à des bouts de visage: oeil, nez, bouche...

    """)
# 20190206-Training of the SDPC model on AT&T database-0CFrmgEcGpw.f135.mp4

# for suffix in ['4a', '4b']:
#     s.add_slide(content=s.content_figures(
#         [os.path.join(url_talk, 'boutin-franciosini-ruffier-perrinet-19_figure' + suffix + '.png')], bgcolor="black",
#     title=None, embed=False, height=s.meta['height']*height_ratio),
#            notes="""
#
# Multi-layered unsupervised Learning
#
# Figure 4: Input, features and reconstructed input after the training on the AT&T database.(a) Images pre-processed with Local Contrast Normalization [36]. (b) 32 randomly selectedfirst-layer RFs fromD(1).  (c) First-layer reconstruction, generated by back-projectingγ1into  the  input  space.   (d)  64  second-layer  RFs  (randomly  selected)  of  size  28×28  px,drawn from the effective dictionaryD(2).  (e) Second-layer reconstruction, generated byback-projectingγ2into the input space, showing 3 best examples (left) and the 3 worst.
#
# """)
s.add_slide(content=s.content_figures(
    [os.path.join(figpath_talk, 'PCOMPBIOL-D-19-01811_R2_compressed_Fig' + suffix + '.png') for suffix in ['2', '9']], title=None, fragment=True, height=s.meta['height']*height_ratio)+SDPC_bib,
       notes="""
29

Ces résultats s'étendent aussi bien aux images naturelles qu'à des images de visage et permettent une représentation progressivement
Pendant sa thèse, Victor Boutin a réussi à prouver que ce réseau permettait notamment de ébruiter des images naturelles de façon robuste, comme cet oiseau et sa reconstruction à partir de l'information dans les couches 1 & 2 (colonnes) et respectivement avec ou sans connections ré-entrantes. Ces résultats ont été quantifiés dans les panneaux B & C.

""")
for suffix in ['S4']:
    s.add_slide(content=s.content_figures(
        [os.path.join(figpath_talk, 'PCOMPBIOL-D-19-01811_R2_compressed_Fig' + suffix + '.png')], bgcolor="black",
    title=None, fragment=True, height=s.meta['height']*height_ratio)+SDPC_bib,
           notes="""

30

De façon surprenante, on a aussi vu émerger dans le réseau des pattern de connection qui module lé réponse de neurones voisins, comme par exemple ceux qui sont alignés ou co-circulaires à un bord orienté, de façon similaire à ce que nous avons observé dans V1.

""")
#
# s.add_slide(content=s.content_figures(
#     [os.path.join('https://github.com/VictorBoutin/SPC_2L/raw/master/Savings/Fig/Fig7.png')],
#     title=None, embed=False, height=s.meta['height']*height_ratio)+SDPC_bib,
#        notes="""
#
# """)

# s.add_slide(content=s.content_figures(
#     [os.path.join(url_talk, 'SDPC_' + suffix + '.png') for suffix in ['3', '4']],
#     bgcolor="black", fragment=True,
#     title=None, embed=False, height=s.meta['height']*.75),
#        notes="""
#
# allows for a better classification as here for MNIST digits
# """)

s.close_section()
###############################################################################
# 🏄🏄🏄🏄🏄🏄🏄🏄             Perspectives      10''       🏄🏄🏄🏄🏄🏄🏄🏄
###############################################################################
i_section = 3
###############################################################################
s.open_section()
s.add_slide_outline(i_section, notes="""

31

Malgré la réussite de ce modèle, il reste toutefois de nombreuses perspectives à aborder dans ce domaine de recherche. Notamment, je voudrais revenir au...

""")
#
# fname = os.path.join(home, 'quantic/science/ActiveVision/2020-09-14_IWAI/2020-09-10_video-abstract.mp4')
# s.add_slide(content=f"""<video controls autoplay loop width=60%/><source type="video/mp4" src="{fname}"></video>""",
#             notes="""You can also embed videos.""")

bib = s.content_bib("Emmanuel Daucé, Pierre Albigès & LP", "2020", "Journal of Vision", url="https://laurentperrinet.github.io/publication/dauce-20/")

url_talk = 'https://laurentperrinet.github.io/2020-09-14_IWAI/figures/'

for layer in ['brain', 'pathways']:
    s.add_slide(content=s.content_figures(
                [os.path.join(figpath_talk, f"architecture_vision_{layer}.svg")],
                height=s.meta['height']*height_ratio),
                notes="""

32

... cerveau...

33

... et à l'existence de deux voies de traitement...

34

... ainsi qu'à l'existence d'un forte compression de l'information autour de l'axe optique.

                """)


for url in ['https://laurentperrinet.github.io/2020-09-14_IWAI/figures/CNS-general-II-A.png',
            # 'https://images.theconversation.com/files/277070/original/file-20190529-192383-zy01r.jpg'
            ]:
    fig = s.content_figures([url], bgcolor="black", height=s.meta['height']*height_ratio)

    s.add_slide(content=fig, # + bib,
                notes="""

34

... ainsi qu'à l'existence d'un forte compression de l'information autour de l'axe optique.


35

Imaginons alors une simple expérience psychophysique dans laquelle je vous demande de fixer la croix,

36

 puis de reconnaitre un chiffre en périphérie

38-40

ou au centre...

41-46

si la présentation est rapide, cette tache peut-être difficile, notamment car si le chiffre est en périphérie, sa résolution décroit et donc il ne peut pas être déchiffré (à proprement parler) sans faire une saccade vers la position de ce chiffre. on parle alors d'inférence contre-factuelle, car on doit deviner l'action à mener en devinant la performance obtenue en effectuant cette action. Ce genre de problème est extrêmement courant en vision  d'où l'importance d'introduire ce type d'action dans la vision par ordinateur.
Nous avons alors fait l'hypothèse que les deux voies (ventrale et dorsale) sont dédiées à deux taches différente

                """)

for i in [0, 4, 8, 9]:
    s.add_slide(image_fname=f'{url_talk}film_FIX.png')
    s.add_slide(image_fname=f'{url_talk}film_display{i}.png')
    s.add_slide(image_fname=f'{url_talk}film_display{i}_SAC.png')
    # s.add_slide(image_fname=f'{url_talk}film_ANS.png')



####################### SLIDE B 2 ##################################
subtitle = [': Computational Graph']
for i, fname in enumerate(['fig_methods']): # CNS-what-where-diagram
    s.add_slide(content=s.content_figures(
    [f'{url_talk}{fname}.svg'],
    height=s.meta['height']*height_ratio) + bib,
    notes="""

47

d'un coté, la voie dorsale va identifier à partir de la vision périphérique une estimation de la probabilité de trouver la position d'un objet, indépendamment de son identité. cela permet d'effectuer une saccade qui une fois réalisée permettra de la tester grâce à la voie ventrale.


    """)

#
# ####################### SLIDE B 3 ##################################
# subtitle = [': What']
# for i, fname in enumerate(['CNS-what-diagram']):
#     s.add_slide(content=s.content_figures(
#     [f'{url_talk}{fname}.svg'],
#     # title=title + subtitle[i],
#     height=s.meta['height']*height_ratio) + bib,
#     notes="""
#
#
# WHAT :
#
# On the one side, a ventral pathway predicts the target identity from the current foveal data.
#
# The what pathway is a classic convolutional clasifier.
#
# It shows some translation invariance.
#
# It can quantify its uncertainty.
#
# It monitors the where pathway.
#
#     TODO: mettre le résultat de l'accuracy map pour faire la transition?
#
#
#     """)
#
#
# ####################### SLIDE B 4 ##################################
# subtitle = [': Where']
# for i, fname in enumerate(['fig_where']):
#     s.add_slide(content=s.content_figures(
#     [f'{url_talk}{fname}.svg'],
#     # title=title + subtitle[i],
#     height=s.meta['height']*height_ratio) + bib,
#     notes="""
#
# WHERE :
#
# On the other side, a dorsal pathway utilizes all the peripheral visual data.
#
# Here we make the assumption that the same logpolar compression pattern is conserved from the retina up to the primary motor layers.
# **Each possible future saccade has an expected accuracy, that can be trained from the what pathway output**. To accelerate the training, we use a shortcut that is training the network on a translated accuracy map (with logpolar encoding). The ouput is thus a **logpolar accuracy map**, that tells for each possible visuo-motor displacement the value of the future accuracy.Thus, the saccadic motor ouput (colliculus) shows a similar log-polar compression than the visual input. The saccades are more precise at short than at long distance (and severals accades may be necessary to precisely reach distant targets).
#     """)
# """The prediction takes the form of an **acuracy map**, that predicts the increase of accuracy for different possible saccades.
#
# This accuracy map is organized radially, with a higher spatial definition at the center than at the periphery. """

title = 'Active vision' # meta['sections'][i_section]

#for kind in ['correct', 'error']:
s.add_slide(content=s.content_figures(
[f'{url_talk}CNS-saccade-' + str(idx) + '.png' for idx in [8, 20]],
        # title=title + ': success',
        height=s.meta['height']*.5, transpose=True) + bib,
notes="""

** The effect of a saccade is to bring relevant visual data at the fovea**

(from left to right)

1. The full visual field

2. After a log polar encoding, the peripheral target is less visible

3. this is the true acuracy map

4. this is the predicted acc map

5. this is the visual data collected at the fovea after the saccade.



48

de façon surprenante, nous avons pu montrer qu'une telle prédiction contre-factuelle de la position est possible, même avec des images périphériques très dégradées et permettent aussi d'obtenir une bonne catégorisation

""")

s.add_slide(content=s.content_figures(
[f'{url_talk}CNS-saccade-' + str(idx) + '.png' for idx in [46, 47, 32] ],
        # title=title + ': failure',
        height=s.meta['height']*.6, transpose=True) + bib,
notes="""

49

avec aussi des cas d'erreur, soit dans la prediction (chiffre dans le bruit?), soit dans la précision ou même le classifier.


""")

s.add_slide(content=s.content_figures(
[f'{url_talk}results-IG.png'],
     # title="Effect of eccentricity",
     height=s.meta['height']*height_ratio) + bib,
notes = """

50

de façon cruciale, nous montrons qu'avec une simple saccade et un coût computation minime, on peut couvrir une large surface de l'image. comparés à des algorithmes classiques de localisation / classification comme YOLO, nous obtenons un cout computationnel sous-linéaire grâce à la compression log-polaire.

           """)



s.add_slide(content=s.content_figures(
            [os.path.join(figpath_talk, "2020-05-20_AAPG2020_AgileNeuroBot.png")],
            height=s.meta['height']*height_ratio),
            notes="""


51

nous avons eu la bonne surprise la semaine dernière d'obtenir un financement ANR pour inclure ce genre d'approches bio-inspirées sur un drone en collaboration avec Stephane Viollet à l'ISM et Ryad Benosman à l'IdV.


            """)

s.close_section()
###############################################################################
# Conclusion - 1''
###############################################################################
###############################################################################
s.open_section()
s.add_slide_summary(title='Conclusion',
    list_of_points =['vision is efficient',
                     'deep learning is great...',
                     '... but predictive coding is better',
                     '... let''s make it active ! '],
                     fragment_type=None,
                     # fragment_type='highlight-green', # BROKEN
    notes="""

52

Pour conclure, la vision est effectivement déraisonnablement efficace, l'apprentissage profond est un bon moyen de s'approcher de cette efficacité - et de nouvelles approches de codage prédictif ou de vision active permettrons je l'espère de bientôt dépasser ces derniers.
""")
s.add_slide(content=intro,
            notes="""

53

Merci pour votre attention! et à mes collaborateurs:

""")

s.add_slide(content=s.content_figures([figname_qr], #title=f"""<a href="{meta['url']}">{meta['url']}</a>""",
 cell_bgcolor=meta['bgcolor'], height=s.meta['height']*height_ratio) + '<BR><a href="{url}"> {url} </a>'.format(url=meta['url']),
            notes="All the material is available online - please flash this code this leads to a page with links to further references and code ")

s.close_section()

###############################################################################
###############################################################################
###############################################################################
###############################################################################
###############################################################################
###############################################################################
###############################################################################
###############################################################################


if slides_filename is None:
    with open("README.md", "w") as text_file:
        text_file.write("""\
# {title}

* What:: talk @ [{conference}{short_conference}]({conference_url})
* Who:: {author}
* Where: {location}, see {url}
* When: {DD:02d}/{MM:02d}/{YYYY}, time: {time_start}-{time_end}

* What:
  * Slides @ https://laurentperrinet.github.io/{tag}
  * Code for slides @ https://github.com/laurentperrinet/{tag}/
  * Abstract: {abstract}

""".format(**meta))

    with open("/tmp/talk.bib", "w") as text_file:
        text_file.write("""\
@inproceedings{{{tag},
    Author = "{author}",
    Booktitle = "{conference}",
    Title = "{title}",
    Abstract = "{abstract}",
    Url = "{url}",
    Year = "{YYYY}",
    Date = "{YYYY}-{MM:02d}-{DD:02d}",
    location = "{location}",
    projects = "{projects}",
    time_start = "{YYYY}-{MM:02d}-{DD:02d}T{time_start}",
    time_start = "{YYYY}-{MM:02d}-{DD:02d}T{time_end}",
    url = "{url}",
    url_slides = "https://laurentperrinet.github.io/{tag}",
    url_code = "https://github.com/laurentperrinet/{tag}/",
}}

""".format(**meta))

else:
    s.compile(filename=slides_filename)

# Check-list:
# -----------
#
# * (before) bring miniDVI adaptors, AC plug, remote, pointer
# * (avoid distractions) turn off airport, screen-saver, mobile, sound, ... other running applications...
# * (VP) open monitor preferences / calibrate / title page
# * (timer) start up timer
# * (look) @ audience
#
# Preparing Effective Presentations
# ---------------------------------
#
# Clear Purpose - An effective image should have a main point and not be just a collection of available data. If the central theme of the image isn't identified readily, improve the paper by revising or deleting the image.
#
# Readily Understood - The main point should catch the attention of the audience immediately. When trying to figure out the image, audience members aren't fully paying attention to the speaker - try to minimize this.
#
# Simple Format - With a simple, uncluttered format, the image is easy to design and directs audience attention to the main point.
#
# Free of Nonessential Information - If information doesn't directly support the main point of the image, reserve this content for questions.
#
# Digestible - Excess information can confuse the audience. With an average of seven images in a 10-minute paper, roughly one minute is available per image. Restrict information to what is extemporaneously explainable to the uninitiated in the allowed length of time - reading prepared text quickly is a poor substitute for editing.
#
# Unified - An image is most effective when information is organized around a single central theme and tells a unified story.
#
# Graphic Format - In graphs, qualitative relationships are emphasized at the expense of precise numerical values, while in tables, the reverse is true. If a qualitative statement, such as "Flow rate increased markedly immediately after stimulation," is the main point of the image, the purpose is better served with a graphic format. A good place for detailed, tabular data is in an image or two held in reserve in case of questions.
#
# Designed for the Current Oral Paper - Avoid complex data tables irrelevant to the current paper. The audience cares about evidence and conclusions directly related to the subject of the paper - not how much work was done.
#
# Experimental - There is no time in a 10-minute paper to teach standard technology. Unless the paper directly examines this technology, only mention what is necessary to develop the theme.
#
# Visual Contrast - Contrasts in brightness and tone between illustrations and backgrounds improves legibility. The best color combinations include white letters on medium blue, or black on yellow. Never use black letters on a dark background. Many people are red/green color blind - avoid using red and green next to each other.
#
# Integrated with Verbal Text - Images should support the verbal text and not merely display numbers. Conversely, verbal text should lay a proper foundation for each image. As each image is shown, give the audience a brief opportunity to become oriented before proceeding. If you will refer to the same image several times during your presentation, duplicate images.
#
# Clear Train of Thought - Ideas developed in the paper and supported by the images should flow smoothly in a logical sequence, without wandering to irrelevant asides or bogging down in detail. Everything presented verbally or visually should have a clear role supporting the paper's central thesis.
#
# Rights to Use Material - Before using any text, image, or other material, make sure that you have the rights to use it. Complex laws and social rules govern how much of someone's work you can reproduce in a presentation. Ignorance is no defense. Check that you are not infringing on copyright or other laws or on the customs of academic discourse when using material.
#
# http://pne.people.si.umich.edu/PDF/howtotalk.pdf
#
