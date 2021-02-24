import pandas as pd
from os import listdir, chdir
from sys import argv
from run_qcore import *


def get_results(xyz_fp: str, epsilon: float, gb_parameter: dict) -> dict:

    chdir(xyz_fp)
    results_dict = {}

    for files_xyz in sorted(listdir(xyz_fp)):
        if files_xyz.endswith(".xyz"):
            filename = files_xyz.split(".")[0]
            results_dict[filename] = qcore_energies(files_xyz, epsilon, gb_parameter)

    return results_dict


def get_xyz_fp():

    global _xyz_fp

    # _xyz_fp = argv[1]
    # _xyz_fp = "/Users/eh19686/Documents/PhD/MNSol_database/subset_water_benzene/benzene"
    _xyz_fp = "/Users/eh19686/Documents/PhD/MNSol_database/parameterisation/solvents_param/neutrals/subset1_solvents/ethanol"

    return _xyz_fp

