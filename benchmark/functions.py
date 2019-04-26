import numpy as np


class ObjectiveFunction(object):
    def __init__(self, name, dimensions, bounds):
        self.name = name
        self.min = bounds[0]
        self.max = bounds[1]
        self.dimensions = dimensions

        self.__evaluations = 0

    @property
    def evaluations(self):
        return self.__evaluations

    def random_region_scaling(self):
        a = self.max / 2.0
        b = self.max
        return np.random.uniform(a, b, self.dimensions)

    def __call__(self, x):
        self.__evaluations += 1
        return self.run(x)

    @np.vectorize
    def evaluate(self, x, y):
        return self(np.array([x, y]))


class SphereFunction(ObjectiveFunction):
    def __init__(self, dim):
        super(SphereFunction, self).__init__('Sphere', dim, (-100.0, 100.0))

    def run(self, x):
        return (x ** 2).sum()


class RosenbrockFunction(ObjectiveFunction):
    def __init__(self, dim):
        super(RosenbrockFunction, self).__init__('Rosenbrock', dim, (-30.0, 30.0))

    def run(self, x):
        a = x[1:] - (x[:-1] ** 2)
        b = x[:1] - 1
        y = 100 * (a ** 2) + (b ** 2)

        return y.sum()


class RastriginFunction(ObjectiveFunction):
    def __init__(self, dim):
        super(RastriginFunction, self).__init__('Rastrigin', dim, (-5.12, 5.12))

    def run(self, x):
        y = (x ** 2) - 10 * np.cos(2.0 * np.pi * x) + 10
        return y.sum()
