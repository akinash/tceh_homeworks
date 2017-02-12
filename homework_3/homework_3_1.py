import random

def random_exception():
    random_key = random.choice([1,2,3])

    if random_key == 1:
        raise ValueError('ValueError')
    elif random_key == 2:
        raise TypeError('TypeError')
    else:
        raise RuntimeError('RuntimeError')

try:
    random_exception()
except ValueError:
    print('ValueError')
except TypeError:
    print('TypeError')
except RuntimeError:
    print('RuntimeError')

