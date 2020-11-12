from apf.core.step import GenericStep
import logging
from apf.producers import KafkaProducer
import os
import datetime


class DummyStep(GenericStep):
    """DummyStep Description

    Parameters
    ----------
    consumer : GenericConsumer
        Description of parameter `consumer`.
    **step_args : type
        Other args passed to step (DB connections, API requests, etc.)

    """
    def __init__(self,consumer = None, config = None,level = logging.INFO,**step_args):
        super().__init__(consumer,config=config, level=level)
        self.producer = KafkaProducer(self.config["PRODUCER_CONFIG"])

    def execute(self,message):
        self.logger.debug(message["alertId"])
        self.producer.produce(message)
