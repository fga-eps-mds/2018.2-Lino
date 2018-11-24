from rasa_core.actions.action import Action
import time
import datetime

DOC_1 = 'login/index.html?response_type=code&'
DOC_2 = 'client_id=102&redirect_uri=/documentodigital/index.html'
UNB_URL = f'https://servicos.unb.br/dados/{DOC_1}{DOC_2}'
GIT_URL = 'https://raw.githubusercontent.com/fga-eps-mds/2018.2-Lino/'
IMGS_PATH = 'master/rasa/images/RegularProof/'


class ActionRegularProof(Action):
    def name(self):
        return "action_regular_proof"

    def run(self, dispatcher, tracker, domain):
        messages = []

        welcome_1 = 'Para conseguir um comprovante de aluno regular '
        welcome_2 = 'você deve acessar este link:'

        messages.append('Só um segundo, to buscando aqui...')
        messages.append(f'{welcome_1}{welcome_2}')
        messages.append(UNB_URL)

        for message in messages:
            dispatcher.utter_message(message)

        # Free cache images
        timestamp = datetime.datetime.now().strftime("%d-%m-%Y")
        free_cache_url = f'?time={timestamp}'

        # typing
        time.sleep(0.5)

        steps = []

        # Step 1
        step_1_1 = 'Faça login no site'
        step_1_2 = 'selecione Declaração de aluno regular'
        step_1 = {
            'text': f'Passo 1: {step_1_1} e {step_1_2}',
            'image': f'{GIT_URL}{IMGS_PATH}step2.png{free_cache_url}'
            }
        steps.append(step_1)

        # Step 2
        step_2_1 = 'Prove que você está ciente do que está fazendo'
        step_2_2 = 'clique em emitir'
        step_2 = {
            'text': f'Passo 2: {step_2_1} e {step_2_2}',
            'image': f'{GIT_URL}{IMGS_PATH}step4.png{free_cache_url}'
        }
        steps.append(step_2)

        # Step 3
        step_3 = {
            'text': 'Passo 3: Agora é so baixar'
        }
        steps.append(step_3)

        for step in steps:
            dispatcher.utter_response(step)

        dispatcher.utter_message(';)')

        return []
