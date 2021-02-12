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


    def test_get_xyz_fp(self):
        fp = "/Users/eh19686/Documents/PhD/MNSol_database/subset_water_benzene/benzene"
        xyz_fp = run_with_sysargv(get_xyz_fp, [fp])

        self.assertEqual(xyz_fp, fp)


    def test_results(self):

        xyz_fp = "/Users/eh19686/Documents/PhD/MNSol_database/subset_water_benzene/benzene"

        radial_shift = -0.2
        epsilon = 2.0

        results_dict = get_results(xyz_fp, epsilon, radial_shift)
        print(results_dict)

        self.assertEqual(type(results_dict), dict)


    if __name__ == '__main__':
        unittest
