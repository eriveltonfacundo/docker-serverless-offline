import ptvsd
from . import handler

ptvsd.enable_attach(address=('0.0.0.0', 5678), redirect_output=True)
ptvsd.wait_for_attach()


def hello(event, context):
    return handler.hello(event, context)
