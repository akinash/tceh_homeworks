def random_exception():
    import random
    random_key = random.choice([1,2,3])
    print(random_key)

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

