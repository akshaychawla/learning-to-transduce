from __future__ import absolute_import
from ..models import Model
import itertools

class SGD(object):
    """
    Stochastic Gradient Descent optimiser.
    """

    def __init__(self, alpha=0.001, name="opt_sgd"):
        self.alpha = alpha
        self.name = name
        self.counter = 0

    def update(self, model):
        assert isinstance(model, Model)

        for lname, layer in model.layers.iteritem():
            weights = layer.return_weights()
            w_grads = layer.return_grads()

            if weights is None:
                continue

            new_weights = []
            for w, g in itertools.izip(weights, w_grads):
                assert w.shape == g.shape, "weights and grads shape do not match during update"
                w -= g/model.batch_size
                new_weights.append(w)

            layer.set_weights(new_weights)

        self.counter += 1

def sgd_test():
    pass
