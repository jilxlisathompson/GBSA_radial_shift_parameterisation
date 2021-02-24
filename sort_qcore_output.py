from getters import *
import numpy as np
import pandas as pd


def make_results_df(gb_parameter: list, epsilon: float) -> dict:

    _xyz_fp = get_xyz_fp()

    results_dict = get_results(_xyz_fp, epsilon, gb_parameter)
    results_from_dict = pd.DataFrame.from_dict(results_dict, orient="index")

    results_df = pd.DataFrame(data=results_from_dict, columns=["FileHandle", "cosmo_energy", "gb_energy"])
    results_df["FileHandle"] = results_df.index
    results_df.reset_index(inplace=True)

    return results_df


def error_DGsolv(gb_parameter: list, epsilon: float) -> np.array:

    qcore_data = make_results_df(gb_parameter, epsilon)

    error_dgsolv = []

    for index, row in qcore_data.iterrows():

        errorDGsolv_idx = row['cosmo_energy'] - row['gb_energy']
        error_dgsolv.append(errorDGsolv_idx)

    return error_dgsolv


