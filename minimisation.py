import sort_qcore_output
from numpy import dot
from scipy.optimize import minimize


def objective_function(gb_parameter: float, epsilon: float) -> list:

    print(f"radial_shift = {gb_parameter}")

    gb_parameter = float(gb_parameter)
    errorDGsolv = sort_qcore_output.error_DGsolv(gb_parameter, epsilon)

    return dot(errorDGsolv, errorDGsolv)


def perform_minimise(epsilon: float):

    x0 = -0.15

    res = minimize(objective_function, x0, args=epsilon, method='nelder-mead', options={"disp": True})

    parameters = res.x
    print(res.x)

    return parameters

