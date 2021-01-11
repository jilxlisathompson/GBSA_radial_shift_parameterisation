from getters import *
import unittest
import sys


def run_with_sysargv(func, sys_argv):
    def patched_func(*args, **kwargs):

        old_sys_argv = list(sys.argv)
        sys.argv = sys_argv
        try:
            return func(*args, **kwargs)
        except Exception as err:
            sys.argv = old_sys_argv
            raise err
        return patched_func()


class TestGetters(unittest.TestCase):

    def test_epsilon(self):
        excel_data_fp = get_experimental_data_fp()

        experimental_data = get_experimental_data(excel_data_fp)

        solvent = "water"
        eps = get_epsilon(experimental_data, solvent)

        epsilon = eps[solvent]

        self.assertEqual(epsilon, 78.36)

    def test_get_xyz_fp(self):
        fp = "/Users/eh19686/Documents/PhD/MNSol_database/subset_water_benzene/benzene"
        xyz_fp = run_with_sysargv(get_xyz_fp, [fp])

        self.assertEqual(xyz_fp, fp)

    def test_get_solvent(self):
        # TODO figure out a good test
        solvent = get_solvent()

        self.assertNotEqual(solvent, "benzene", msg='Equal')

    def test_get_results(self):
        excel_data_fp = get_experimental_data_fp()

        experimental_data = get_experimental_data(excel_data_fp)

        solvent = "water"
        eps = get_epsilon(experimental_data, solvent)

        epsilon = eps[solvent]
        xyz_fp = "/Users/eh19686/Documents/PhD/MNSol_database/subset_water_benzene/benzene"

        radial_shift = 1.2

        results_dict = get_results(xyz_fp, epsilon, radial_shift)
        print(results_dict)

        self.assertEqual(type(results_dict), dict)



    if __name__ == '__main__':
        unittest
