FROM jagregory/pandoc:latest

MAINTAINER Brian Lin <blin@cs.wisc.edu>

RUN apt-get update -y \
    && apt-get install -y python-pip curl

RUN pip install mkdocs MarkdownHighlight pygments

COPY convert-twiki /usr/local/bin/
COPY convert-twiki-list /usr/local/bin/
COPY osg-conversions.py /usr/local/bin/

ENTRYPOINT []
CMD PYTHONPATH=src/ mkdocs serve --dev-addr 0.0.0.0:8000
