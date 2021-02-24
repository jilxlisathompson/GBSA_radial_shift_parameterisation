import sort_qcore_output
from numpy import dot
from scipy.optimize import minimize
import numpy as np


def objective_function(gb_parameter: list, epsilon: float) -> list:

    errorDGsolv = sort_qcore_output.error_DGsolv(gb_parameter, epsilon)

    return dot(errorDGsolv, errorDGsolv)


def perform_minimise(epsilon: float):

    x0 = np.array([-0.15, 1.0])

    res = minimize(objective_function, x0, args=epsilon, method='nelder-mead', options={"disp": True})

    parameters = res.x
    print(res.x)

    return parameters

