FROM python:3.6

RUN apt-get install -y git

RUN pip install rasa_core==0.10.3

RUN pip install rasa_nlu[spacy] && \
    python -m spacy download pt && \
    python -m spacy download en

RUN pip install rasa_nlu[tensorflow]

RUN mkdir /2018.2-Lino

ADD . /2018.2-Lino

WORKDIR /2018.2-Lino/rasa

ENV TRAINING_EPOCHS=300 \
    CREDENTIALS="./rasa/credentials.yml"

CMD sleep infinity
