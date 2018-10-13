FROM python:3.6

ADD ./requirements.txt /tmp

RUN pip install -r /tmp/requirements.txt  && \
    python -m spacy download pt && \
    python -m spacy download en

RUN pip install rasa_nlu[tensorflow]

RUN pip install pymongo
RUN pip install requests
RUN pip install httpretty

RUN mkdir /2018.2-Lino

ADD . /2018.2-Lino

WORKDIR /2018.2-Lino/rasa

ENV TRAINING_EPOCHS=300 \
    CREDENTIALS="credentials.yml"

CMD python -m rasa_core.run -d models/dialogue -u models/nlu/default/current --port 5002 -c telegram --credentials credentials.yml
