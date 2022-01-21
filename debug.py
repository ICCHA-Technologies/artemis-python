import logging
import sys


def Debugin():
    console = logging.StreamHandler()
    console.setFormatter(logging.Formatter('[%(asctime)s] %(name)-12s %(levelname)-8s %(message)s'))
    logging.getLogger().addHandler(console)
    logging.getLogger().setLevel(logging.DEBUG)
    LOGGER = logging.getLogger('Server Stomp')