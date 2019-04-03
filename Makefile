NAME=slides.py

default: github

edit:
	atom src/slides/slides.py example.py

html:
	python3 example.py

github: html
	git commit --dry-run -am 'Test' | grep -q -v 'nothing to commit' && git commit -am' updating slides'
	git push
	open https://laurentperrinet.github.io/$(NAME)

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
