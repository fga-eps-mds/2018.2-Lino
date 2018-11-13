from rasa_core.actions.action import Action

DOC_1 = 'login/index.html?response_type=code&'
DOC_2 = 'client_id=102&redirect_uri=/documentodigital/index.html'
UNB_URL = 'https://servicos.unb.br/dados/{DOC_1}{DOC_2}'
GIT_URL = 'https://github.com/'
IMG_PATH = ''


class ActionRegisterProof(Action):
    def name(self):
        return "action_register_proof"

    def run(self, dispatcher, tracker, domain):
        messages = []

        messages.append('Só um segundo, to buscando aqui...')
        messages.append('Para conseguir um comprovante de matrícula: ')
        messages.append('você deve acessar esse link')
        messages.append(f'{UNB_URL}')

        for message in messages:
            dispatcher.utter_message(message)

        return []
