FROM jagregory/pandoc:latest

MAINTAINER Brian Lin <blin@cs.wisc.edu>

RUN apt-get update -y \
    && apt-get install -y python-pip python-lxml

RUN pip install mkdocs MarkdownHighlight pygments

COPY gettwikipage /usr/local/bin/
COPY convert-twiki /usr/local/bin/

ENTRYPOINT []
CMD mkdocs serve --dev-addr 0.0.0.0:8000
