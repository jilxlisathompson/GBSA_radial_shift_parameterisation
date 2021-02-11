import json
import subprocess
from prep_input import *
from getters import *


def run_qcore(filename: str, epsilon: float, radial_shift: float) -> str:
    """
    function that runs qcore for cosmo and gb
    and extracts electrostiatic energy from output
    """

    qcore_input_command_str = qcore_run_command()

    solvation_input = qcore_input(filename, epsilon, radial_shift)

    qcore_output_solvation = subprocess.run(qcore_input_command_str +
                                            '"' + solvation_input
                                            + '"',
                                            capture_output=True, text=True, shell=True)
    print(qcore_output_solvation.stderr)

    if qcore_output_solvation.returncode == 0 :
        return qcore_output_solvation.stdout
    elif qcore_output_solvation.returncode != 0 :
        return qcore_output_solvation.stderr


def get_qcore_energies(filename: str, epsilon: float, radial_shift: float) -> dict:

    qcore_output_solvation, qcore_output_gas = run_qcore(filename, epsilon, radial_shift)
    qcore_results_solvation = json.loads(qcore_output_solvation)
    qcore_results_gas = json.loads(qcore_output_gas)
    gas_energy = qcore_results_gas["xtb_run"]["energy"]
    esolv_energy = qcore_results_solvation["gb_run"]["energy"]
    gsolv = esolv_energy - gas_energy

    return {"gas": gas_energy, "Esolv": esolv_energy, "DGsolv":gsolv }

