from rasa_core.actions.action import Action

DOC_1 = 'login/index.html?response_type=code&'
DOC_2 = 'client_id=102&redirect_uri=/documentodigital/index.html'
UNB_URL = f'https://servicos.unb.br/dados/{DOC_1}{DOC_2}'
GIT_URL = 'https://raw.githubusercontent.com/fga-eps-mds/2018.2-Lino/'
IMGS_PATH = 'Issue_204-HourGridStatementFlow/rasa/images/schedule/'


class ActionSchedule(Action):
    def name(self):
        return "action_schedule"

    def run(self, dispatcher, tracker, domain):
        messages = []

        messages.append('Só um segundo, to buscando aqui...')
        messages.append('Pra pegar sua grade horária: ')
        messages.append('você deve acessar este link')
        messages.append(UNB_URL)

        for message in messages:
            dispatcher.utter_message(message)

        steps = []

        step_1 = {
            'text': 'Passo 1: Faça login no site.',
            'image': f'{GIT_URL}{IMGS_PATH}step1.png'
            }
        steps.append(step_1)

        step_2 = {
            'text': 'Passo 2: Selecione grade horária',
            'image': f'{GIT_URL}{IMGS_PATH}step2.png'
        }
        steps.append(step_2)

        step_3 = {
            'text': 'Passo 3: Prove que você está ciente do que está fazendo',
            'image': f'{GIT_URL}{IMGS_PATH}step3.png'
        }
        steps.append(step_3)

        step_4 = {
            'text': 'Passo 4: Clique em emitir',
            'image': f'{GIT_URL}{IMGS_PATH}step4.png'
        }
        steps.append(step_4)

        step_5 = {
            'text': 'Passo 5: Agora é so baixar',
            'image': f'{GIT_URL}{IMGS_PATH}step5.png'
        }
        steps.append(step_5)

        for step in steps:
            dispatcher.utter_response(step)
        
        
        return []