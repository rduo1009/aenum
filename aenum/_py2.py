from operator import div as _div_
from inspect import getargspec

def raise_with_traceback(exc, tb):
    if sys.version_info[0] == 2:
        exec("raise exc, None, tb")
    else:
        raise exc.with_traceback(tb)

__all__ = ['_div_', 'getargspec', 'raise_with_traceback']
