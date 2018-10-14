import time


def timed(f):
    def _timed(*args, **kwargs):
        start = time.time()
        result = f(*args, **kwargs)
        t = (time.time() - start) * 1000
        print("runtime for function {}: {:0.4f}".format(f.__name__, t))
        return result

    return _timed
