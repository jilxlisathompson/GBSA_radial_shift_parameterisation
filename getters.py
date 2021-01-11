from run_qcore import *
import pandas as pd
from os import listdir, chdir
from sys import argv


def get_results(xyz_fp: str, epsilon: float, radial_shift: float) -> dict:
    # TODO read MNsol database data into pandas dataframe
    # TODO write function that reads data and call
    # TODO get filenames for run

    print(f"in get_results, radial_shift = {radial_shift}")
    chdir(xyz_fp)
    results_dict = {}

    for files_xyz in sorted(listdir(xyz_fp)):
        if files_xyz.endswith(".xyz"):
            filename = files_xyz.split(".")[0]
            results_dict[filename] = get_qcore_energies(files_xyz, epsilon, radial_shift)

    return results_dict


def get_experimental_data(excel_data_fp: str) -> dict:
    solvent = get_solvent()
    print(f"solvent = {solvent}")
    print("in get_experimental_data")
    experimental_data_df = pd.read_excel(excel_data_fp)
    new_exp_df = experimental_data_df[(experimental_data_df["Solvent"] == solvent) & (experimental_data_df["Charge"] == 0)]
    print("ENDSDDDDDD")
    return new_exp_df


def get_epsilon(experimental_data_df: dict, solvent: str) -> dict:

    solvent_index = experimental_data_df.index[experimental_data_df['Solvent'] == solvent].tolist()[-1]
    
    epsilons = experimental_data_df["eps"]
    epsilon = epsilons[solvent_index]

    return {solvent: epsilon}


# TODO make into lambda function
def get_solvent() -> str:

    global solvent
    xyz_fp = get_xyz_fp()
    print("In get solvent")
    print(f"xyz_fp = {xyz_fp}")
    solvent = xyz_fp.split("/")[-2]

    return solvent


def get_xyz_fp():
    global _xyz_fp

    _xyz_fp = argv[1]

    return _xyz_fp


# TODO change hardcoded shizz
def get_experimental_data_fp():
   # global _excel_data_fp

    _excel_data_fp = "/home/eh19686/gbsa_parameterisation/MNSol_alldata.xls"
    return _excel_data_fp
