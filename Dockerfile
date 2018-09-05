FROM python:3.6

RUN apt-get install -y git

RUN pip install rasa_core && \
    pip install -r dev-requirements.txt && \
    pip install -e .

RUN pip install rasa-nlu[spacy]==0.13.0 && \
    python -m spacy download pt

RUN pip uninstall -y tensorflow && pip install tensorflow==1.5

RUN mkdir /2018.2-Lino

ADD ./2018.2-Lino /2018.2-Lino

WORKDIR /2018.2-Lino

ENV TRAINING_EPOCHS=300
CMD python train.py all
