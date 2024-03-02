FROM hemanhp/djbase:4.2.7

COPY ./requirements /requirements
COPY ./src /src

WORKDIR /src

EXPOSE 8000

RUN /py/bin/pip install -r /requirements/development.txt

ENV PATH="/py/bin:$PATH"