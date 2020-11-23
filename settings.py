##################################################
#       rate_producer_step   Settings File
##################################################

import os
from schema import SCHEMA

# Consumer configuration
# Each consumer has different parameters and can be found in the documentation-
CONSUMER_CONFIG = {
    "PARAMS": {
        "bootstrap.servers": os.environ["CONSUMER_SERVER"],
        "group.id": os.environ["CONSUMER_GROUP_ID"]
    },
    "TOPICS": os.environ["CONSUMER_TOPICS"].strip().split(",")
}

PRODUCER_CONFIG = {
    "TOPIC": os.environ["PRODUCER_TOPIC"],
    "PARAMS": {
        'bootstrap.servers': os.environ["PRODUCER_SERVER"],
    },
    "SCHEMA": SCHEMA,
}

# Step Configuration
STEP_CONFIG = {
    "PRODUCER_CONFIG": PRODUCER_CONFIG,
}

LOGGING_DEBUG = False
