FROM python:3.6

ADD ./requirements.txt /tmp

RUN pip install -r /tmp/requirements.txt  && \
    python -m spacy download pt

RUN pip uninstall -y tensorflow && pip install tensorflow==1.5

RUN mkdir /2018.2-Lino

ADD . /2018.2-Lino

WORKDIR /2018.2-Lino/rasa

ENV TRAINING_EPOCHS=450 \
    CREDENTIALS="credentials.yml"

<<<<<<< HEAD
CMD python3 train-telegram.py
=======
CMD python train-telegram.py
>>>>>>> 1a23b86c5cf7d3b0bcede4a93bbf950471641bb5
