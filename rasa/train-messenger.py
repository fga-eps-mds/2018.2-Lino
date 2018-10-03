
import logging
import os
import yaml
import train

from rasa_core import utils
from rasa_core.interpreter import RasaNLUInterpreter
from rasa_core.agent import Agent
from rasa_core.interpreter import RegexInterpreter
from rasa_core.channels import HttpInputChannel
from rasa_core.channels.facebook import FacebookInput
from rasa_core.policies.fallback import FallbackPolicy
from rasa_core.policies.keras_policy import KerasPolicy
from rasa_core.policies.memoization import MemoizationPolicy


logger = logging.getLogger(__name__)

VERIFY = os.getenv('VERIFY', '')
SECRET = os.getenv('SECRET', '')
PAGE_ACCESS_TOKEN = os.getenv('PAGE_ACCESS_TOKEN', '')


def run():
    # load your trained agent
    interpreter = RasaNLUInterpreter('models/nlu/default/current')

    agent = Agent.load("models/dialogue", interpreter=RegexInterpreter())

    input_channel = FacebookInput(
        fb_verify=VERIFY,  # you need tell facebook this token, to confirm your URL
        fb_secret=SECRET,  # your app secret
        fb_access_token=PAGE_ACCESS_TOKEN  # token for the page you subscribed to
    )

    agent.handle_channel(HttpInputChannel(5001, "", input_channel))



if __name__ == '__main__':
    utils.configure_colored_logging(loglevel='DEBUG')

    logger.info("Train NLU")
    train.train_nlu()
    logger.info("Train Dialogue")
    train.train_dialogue()
    logger.info("Run")
    run()
