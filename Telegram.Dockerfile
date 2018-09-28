FROM python:3.6

ADD ./req.txt /tmp

RUN pip install -r /tmp/req.txt  && \
    python -m spacy download pt && \
    python -m spacy download en

RUN pip uninstall -y tensorflow && pip install tensorflow==1.5

RUN mkdir /2018.2-Lino

ADD . /2018.2-Lino

WORKDIR /2018.2-Lino/rasa

ENV TRAINING_EPOCHS=300 \
    CREDENTIALS="credentials.yml"

EXPOSE 5002:5002

CMD python3 train-telegram.py all