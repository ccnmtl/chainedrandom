import random


class Response:
    def __init__(self, **kwargs):
        self.seed = kwargs['seed']
        self.next_seed = kwargs['next_seed']
        self.n = kwargs['n']
        self.values = kwargs['values']


class ChainedRandom:
    def __init__(self, seed=None):
        if seed is None:
            seed = str(random.random())
        random.seed(str(seed))
        self.next_seed = seed

    def rand_n(self, n):
        return self.randint(a=0, b=n, n=1).values[0]

    def randint(self, a=0, b=10, n=1):
        random.seed(str(self.next_seed))
        values = []
        for i in range(n):
            values.append(random.randint(int(a), int(b)))
        seed_used = self.next_seed
        next_seed = str(random.random())
        self.next_seed = next_seed
        return Response(
            **dict(
                values=values,
                a=a,
                b=b,
                n=n,
                seed=seed_used,
                next_seed=next_seed,
                ))
