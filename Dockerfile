FROM python:3.6

RUN apt-get install -y git

RUN pip install rasa_core==0.10.3

RUN pip install rasa-nlu[spacy]==0.13.0 && \
    python -m spacy download pt

RUN pip uninstall -y tensorflow && pip install tensorflow==1.5

RUN mkdir /2018.2-Lino

WORKDIR /2018.2-Lino
