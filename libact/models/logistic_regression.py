from libact.base.interfaces import ContinuousModel
import sklearn.linear_model
import numpy as np


class LogisticRegression(ContinuousModel):

    def __init__(self, *args, **kwargs):
        self.model = sklearn.linear_model.LogisticRegression(*args, **kwargs)

    def train(self, dataset, *args, **kwargs):
        return self.model.fit(*(dataset.format_sklearn() + args), **kwargs)

    def predict(self, feature, *args, **kwargs):
        return self.model.predict(feature, *args, **kwargs)

    def score(self, testing_dataset, *args, **kwargs):
        return self.model.score(*(testing_dataset.format_sklearn() + args), **kwargs)

    def predict_real(self, feature, *args, **kwargs):
        return self.model.predict_proba(feature, *args, **kwargs)
