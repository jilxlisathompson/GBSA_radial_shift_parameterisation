import minimisation
import run_all_structures
from pandas import ExcelWriter
from os import path
from getters import *


def main():

    parameters = minimisation.perform_minimise()
    solvent = get_solvent()
    with open(f"../parameters_{solvent}.txt", "w") as file:
        file.write(f"solvent = {solvent}")
        file.write(f"parameterised radial shift = {str(parameters[0])}")
if __name__ == "__main__":
    main()

