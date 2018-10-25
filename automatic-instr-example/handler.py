from thundra.thundra_agent import Thundra
import functions

thundra = Thundra()


@thundra
def handler(event, context):
    functions.first_func(500)
    functions.fourth_func()
    return {
        'message': 'Your demo function ran successfully'
    }
