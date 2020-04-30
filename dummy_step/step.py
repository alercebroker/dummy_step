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
        self.producer.produce(message)

    
    def send_metrics(self, **metrics):
        """
        Override the default send_metrics to set a different name
        for each dummy_step instead of all having the same name
        wich is self.__class__.__name__
        """
        if self.elastic_search:
            source = os.getenv("STEP_NAME", self.__class__.__name__)
            date = datetime.datetime.now(
                datetime.timezone.utc).strftime("%Y%m%d")
            index_prefix = self.config["ES_CONFIG"].get(
                "INDEX_PREFIX", "pipeline")
            self.index = f"{index_prefix}-{source.lower()}-{date}"
            metrics["source"] = source
            self.elastic_search.index(index=self.index, body=metrics)