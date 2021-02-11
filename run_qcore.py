import json
import subprocess
from prep_input import *
from getters import *


def run_qcore(filename: str, epsilon: float, gb_parameter: float) -> str:
    """
    function that runs qcore for cosmo and gb
    and extracts electrostiatic energy from output
    """


    qcore_input_command_str = qcore_run_command()

    solvation_input = qcore_input(filename, epsilon, gb_parameter)

    qcore_output_solvation = subprocess.run(qcore_input_command_str +
                                            '"' + solvation_input
                                            + '"',
                                            capture_output=True, text=True, shell=True)

    if qcore_output_solvation.returncode == 0:
        return qcore_output_solvation.stdout
    elif qcore_output_solvation.returncode != 0:
        return qcore_output_solvation.stderr


def qcore_energies(filename: str, epsilon: float, radial_shift: float) -> dict:

    qcore_output_solvation = run_qcore(filename, epsilon, radial_shift)

    qcore_results_solvation = json.loads(qcore_output_solvation)

    gb_energy = qcore_results_solvation["gb_run"]["solvation_energy"]
    cosmo_energy = qcore_results_solvation["cosmo_run"]["solvation_energy"]

    return {"cosmo_energy": cosmo_energy, "gb_energy": gb_energy}

