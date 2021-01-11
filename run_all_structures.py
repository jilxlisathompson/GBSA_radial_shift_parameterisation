from getters import *
import numpy as np
import pandas as pd

def make_results_df(radial_shift: float) -> dict:

    _xyz_fp = get_xyz_fp()
    solvent = get_solvent()
    _excel_data_fp = get_experimental_data_fp()
    kcal2hartree = 0.0015936876349818203
    print("here in make_results_df")
    print(get_experimental_data(_excel_data_fp))
    print("out of it") 
    experimental_df = get_experimental_data(_excel_data_fp)
    epsilon = get_epsilon(experimental_df, solvent)
    epsilon = epsilon[solvent]
    results_dict = get_results(_xyz_fp, epsilon, radial_shift)

    experimental_df["DeltaGsolv"] = kcal2hartree * experimental_df["DeltaGsolv"]
    results_from_dict = pd.DataFrame.from_dict(results_dict, orient="index")

    results_df = pd.DataFrame(data = results_from_dict, columns=["FileHandle", "gas", "Esolv", "DGsolv"])
    results_df["FileHandle"] = results_df.index
    results_df.reset_index(inplace=True)

    all_data_df = experimental_df[["FileHandle", "SoluteName",
                                  "Charge", "DeltaGsolv", "eps", "TotalArea"]]
    all_data_df["qcore_gas"] = results_df["gas"].values.tolist()
    all_data_df["qcore_Esolv"] = results_df["Esolv"].values.tolist()
    all_data_df["qcore_DGsolv"] = results_df["DGsolv"].values.tolist()

    return all_data_df


def get_errorDGsolv(radial_shift: float) -> np.array:

    qcore_data = make_results_df(radial_shift)


    errorDGsolv = []

    for index, row in qcore_data.iterrows():
        errorDGsolv_idx = row['DeltaGsolv'] - row['qcore_DGsolv']
        errorDGsolv.append(errorDGsolv_idx)

    return errorDGsolv


