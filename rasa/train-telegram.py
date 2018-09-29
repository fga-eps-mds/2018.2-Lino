import logging
import os
import yaml
import train

from rasa_core import utils
from rasa_core.interpreter import RasaNLUInterpreter
from rasa_core.agent import Agent
from rasa_core.interpreter import RegexInterpreter
from rasa_core.channels import HttpInputChannel
from rasa_core.channels.telegram import TelegramInput


logger = logging.getLogger(__name__)

CREDENTIALS = os.getenv('CREDENTIALS', 'credentials.yml')
# LINO_PORT = int(os.getenv('LINO_PORT', 5005))

def run():
    interpreter = RasaNLUInterpreter('models/nlu/default/current')

    configs = yaml.load(open(CREDENTIALS))

    agent = Agent.load('models/dialogue', interpreter=RegexInterpreter())

    input_channel = TelegramInput(
        access_token=configs['access_token'],
        verify=configs['verify'],
        webhook_url=configs['webhook_url']
    )

    agent.handle_channel(HttpInputChannel(5002, "" , input_channel))

if __name__ == '__main__':
    utils.configure_colored_logging(loglevel='DEBUG')

    logger.info("Train NLU")
    train.train_nlu()
    logger.info("Train Dialogue")
    train.train_dialogue()
    logger.info("Run")
    run()
