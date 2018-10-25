import time
from thundra.opentracing.tracer import ThundraTracer


def third_func(x):
    tracer = ThundraTracer.get_instance()
    with tracer.start_active_span(operation_name='third_func', finish_on_close=True,
                                  tags={"test_tag": "This is the third function"}) as scope:
        time.sleep(0.1)
        with tracer.start_active_span(operation_name='third_func_child', finish_on_close=True,
                                      tags={"test_tag": "This is the third function child"}) as scope:
            time.sleep(0.3)
            return {
                'third-func': x * 2,
            }


def second_func(x):
    tracer = ThundraTracer.get_instance()
    with tracer.start_active_span(operation_name='second_func', finish_on_close=True,
                                  tags={"test_tag": "This is the second function"}) as scope:
        time.sleep(0.1)
        third_func(x * 2)
        time.sleep(0.4)
        return {
            'second-func': x * 2,
        }


def first_func(x):
    tracer = ThundraTracer.get_instance()
    with tracer.start_active_span(operation_name='first_func', finish_on_close=True,
                                  tags={"test_tag": "This is the first function"}) as scope:
        time.sleep(0.1)
        second_func(x * 2)
        time.sleep(0.1)
        return {
            'first-func': x * 2,
        }


def fourth_func():
    tracer = ThundraTracer.get_instance()
    with tracer.start_active_span(operation_name='fourth_func', finish_on_close=True,
                                  tags={"test_tag": "This is the fourth function"}) as scope:
        time.sleep(1)
        return {
            'fourth-func': 'Hi! I am an independent function',
        }
