def qcore_input(filename: str, epsilon: float, gb_parameter: dict) -> str:

    print(f"{filename}")
    print(gb_parameter[0])

    qcore_input_str_calc = """xtb_run := xtb(structure(file ='{filename}'))
                            cosmo_run := solvation(load = xtb_run
                            model = cosmo 
                            epsilon = {epsilon}
                            switch = 0.3 )
                            gb_run := solvation(load = xtb_run
                            model = gbsa
                            epsilon = {epsilon}
                            radial_factor = {radial_factor}
                            d_parameter = 4.0
                            radial_shift = {radial_shift} bohr)"""\
        .format(filename=filename, epsilon=epsilon, radial_factor=gb_parameter[1],
                radial_shift=gb_parameter[0])
    return qcore_input_str_calc


def qcore_run_command() -> str:

    qcore_locale = "/Users/eh19686/Qcore/cmake-build-release/qcore"

    qcore_run_str = qcore_locale + " -f json -s "

    return qcore_run_str
