class Steel:
    def __init__(self, ex, poisson):
        def f(x):
            return ex
        self.name = 'Steel'
        self.ex = f
        self.poisson = poisson
        self.table = [1, 2]
