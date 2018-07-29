from __future__ import absolute_import
from __future__ import division
from __future__ import unicode_literals

import logging

from rasa_nlu import config
from rasa_nlu.components import ComponentBuilder
from rasa_nlu.model import Trainer
from rasa_nlu.training_data import load_data

if __name__ == '__main__':
    logging.basicConfig(level='INFO')

    builder = ComponentBuilder(
        use_cache=True
    )  # will cache components between pipelines (where possible)

    training_data = load_data('./models/dialogflow/')
    trainer = Trainer(config.load("./nlu_config.yml"), builder)
    trainer.train(training_data)
    model_directory = trainer.persist('./models/nlu/' , fixed_model_name="current")