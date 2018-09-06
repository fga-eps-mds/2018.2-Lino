from python:3.6

run apt-get install -y git

run pip install rasa_core==0.10.3

run pip install rasa_nlu[spacy] && \
    python -m spacy download en_core_web_md && \
    python -m spacy link en_core_web_md en

run pip install rasa_nlu[tensorflow]

run mkdir /2018.2-Lino

copy . .

workdir /2018.2-Lino

# env TRAINING_EPOCHS=300 \
#     CREDENTIALS="./rasa/credentials.yml"

cmd sleep infinity
