train-nlu:
	python -m rasa_nlu.train -c nlu_config.yml --data data/intents/nlu.md -o models --fixed_model_name nlu --project current --verbose

train-core:
	python -m rasa_core.train -d domain.yml -s data/stories/stories.md -o models/dialogue

run-telegram:
	python -m rasa_core.run -d models/dialogue -u models/current/nlu --port 5002 -c telegram --credentials credentials.yml

run-facebook:
	python train.py run-facebook
