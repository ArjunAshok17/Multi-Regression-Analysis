# Program Description #
# Defines the functions necessary to run linear regression on a dataset #

from sklearn import linear_model    # linear regression
from data_management import *        # data management


# returns optimized linear model #
def optimize(input, exp_out):
    # model creation #
    regr_look = linear_model.LinearRegression()
    
    # train #
    regr_look.fit(input, exp_out)

    # return model & parameters #
    return (regr_look, regr_look.coef_)


# conducts predictions for all models #
def regr_prediction(regr_looks, input):
    # make prediction #
    regr_preds = [regr_look.predict(input) for regr_look in regr_looks]

    # return regressive predictions#
    return regr_preds


"""
    The following code is simply to experiment with manually coding gradient descent.
    Coming soon.
"""
