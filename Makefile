default: github

SRC=example

edit:
	atom src/slides/slides.py $(SRC).py

html:
	python3 $(SRC).py index.html

page:
	python3 $(SRC).py
	cat /tmp/talk.bib |pbcopy
	atom ~/pool/blog/perrinet_curriculum-vitae_tex/LaurentPerrinet_Presentations.bib
	# academic ...

show: html
#	open -a firefox $(SRC).html
	open /Applications/Safari.app/Contents/MacOS/Safari  index.html

github: html
	git commit --dry-run -am 'Test' | grep -q -v 'nothing to commit' && git commit -am' updating slides'
	git push
	open http://laurentperrinet.github.io/slides.py/
	# open https://laurentperrinet.github.io/$(SRC)

print: html
	#open -a /Applications/Chromium.app https://laurentperrinet.github.io/$(SRC)/?print-pdf&showNotes=true
	#open "https://laurentperrinet.github.io/$(SRC)/?print-pdf&showNotes=true"
	/Applications/Chromium.app/Contents/MacOS/Chromium --headless --disable-gpu --print-to-pdf=$(SRC).pdf "https://laurentperrinet.github.io/$(SRC)/?print-pdf"


# https://docs.python.org/2/distutils/packageindex.html
pypi_tags:
	git commit -am' tagging for PyPI '
	git tag 0.0.0 -m "Adds a tag so that we can put this on PyPI."
	git push --tags origin master

pypi_push:
	python setup.py register

pypi_upload:
	python setup.py sdist upload

pypi_docs: html
	rm web.zip
	zip web.zip index.html
	open https://pypi.python.org/pypi?action=pkg_edit&name=$NAME

clean:
	rm -fr build dist results/* *.pyc **/*.pyc
