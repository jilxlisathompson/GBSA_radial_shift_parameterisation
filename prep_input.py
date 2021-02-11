def qcore_input(filename: str, epsilon: float, gb_parameter: float) -> str:

    print(f"{filename}")

    qcore_input_str_calc = """xtb_run := xtb(structure(file ='{filename}'))
                            cosmo_run := solvation(load = xtb_run
                            model = cosmo 
                            epsilon = {epsilon}
                            switch = 0.3 )
                            gb_run := solvation(load = xtb_run
                            model = gbsa
                            epsilon = {epsilon}
                            radial_factor = 1.2
                            d_parameter = 4.0
                            radial_shift = {radial_shift} bohr)"""\
        .format(filename=filename, epsilon=epsilon, radial_shift=gb_parameter)
    return qcore_input_str_calc


def qcore_run_command() -> str:

    qcore_locale = "/Users/eh19686/Qcore/cmake-build-release/qcore"

    qcore_run_str = qcore_locale + " -f json -s "

    return qcore_run_str
