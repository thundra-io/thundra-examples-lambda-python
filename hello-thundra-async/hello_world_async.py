from thundra.thundra_agent import Thundra

thundra = Thundra()

@thundra
def handler(event, context):
    response = {
        'message': 'Hello Thundra Async!'
    }
    return response