import time
from thundra.plugins.trace.traceable import Traceable

@Traceable(trace_args=True, trace_return_value=True)
def third_func(x):
    time.sleep(0.3)
    return {
        'third-func': x*2,
    }


@Traceable(trace_args=True, trace_return_value=True)
def second_func(x):
    time.sleep(0.1)
    third_func(x*2)
    time.sleep(0.4)
    return {
        'second-func': x * 2,
    }


@Traceable(trace_args=True, trace_return_value=True)
def first_func(x):
    time.sleep(0.1)
    second_func(x * 2)
    time.sleep(0.1)
    return {
        'first-func': x * 2,
    }

@Traceable(trace_args=True, trace_return_value=True)
def fourth_func():
    time.sleep(1)
    return {
        'fourth-func': 'Hi! I am an independent function',
    }