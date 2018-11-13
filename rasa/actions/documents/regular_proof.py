from rasa_core.actions.action import Action

DOC_1 = 'login/index.html?response_type=code&'
DOC_2 = 'client_id=102&redirect_uri=/documentodigital/index.html'
UNB_URL = f'https://servicos.unb.br/dados/{DOC_1}{DOC_2}'
GIT_URL = 'https://raw.githubusercontent.com/fga-eps-mds/2018.2-Lino/'
IMGS_PATH = ''

class ActionRegularProof(Action):
    def name(self):
        return "action_regular_proof"

    def run(self, dispatcher, tracker, domain):
        messages = []

        messages.append('Só um segundo, to buscando aqui...')
        messages.append('Para conseguir um comprovante de matrícula: ')
        messages.append('você deve acessar este link')
        messages.append(UNB_URL)

        for message in messages:
            dispatcher.utter_message(message)

        return []