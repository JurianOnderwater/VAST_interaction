import time
from functools import wraps

def timerFunc(f: function):
    '''Times decorated function'''
    @wraps(f)
    def wrapper(*args, **kwargs):
        ts = time()
        result = f(*args, **kwargs
        te = time()
        print('func:%r args:[%r, %r] took: %2.4f sec' % \
          (f.__name__, args, kwargs, te-ts))
        return result
    return wrapper