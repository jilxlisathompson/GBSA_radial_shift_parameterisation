import run_all_structures
from numpy import dot
from scipy.optimize import minimize


def objective_function(radial_shift: float) -> list:

    radial_shift = float(radial_shift)
    errorDGsolv = run_all_structures.get_errorDGsolv(radial_shift)
    return dot(errorDGsolv, errorDGsolv)


def perform_minimise():

    x0 = -0.15

    res = minimize(objective_function, x0, method='nelder-mead', options={"disp": True})

    parameters = res.x
    print(res.x)


    return parameters

