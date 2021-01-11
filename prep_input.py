def get_qcore_input(filename: str, epsilon: float, radial_shift: float) -> str:

    qcore_input_str_calc = """gb_run := xtb( 
                            structure(file = '{filename}')
                            solvation(
                            model = gbsa
                            radial_shift = {radial_shift} bohr
                            epsilon= {epsilon}
                            surface_area_factor=0.0
                            probe_radius= 0.0 bohr
                            radial_factor = 1.2
                            d_parameter = 4.0))
                            """.format(filename=filename, epsilon=epsilon, radial_shift=radial_shift)
    return qcore_input_str_calc


def get_qcore_gas_input(filename: str) -> str:

    qcore_input_str_calc = """xtb_run := xtb(structure(file ='{filename}'))
                            """.format(filename=filename)
    return qcore_input_str_calc


def get_qcore_run_command() -> str:
    qcore_locale = "/home/eh19686/Qcore/release/qcore"

    qcore_run_str = qcore_locale + " -f json -s "

    return qcore_run_str
