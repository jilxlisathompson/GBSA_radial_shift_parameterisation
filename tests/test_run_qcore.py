import unittest
from prep_input import *
from run_qcore import *
import os
import json


class TestRunQcore(unittest.TestCase):

    def test_qcore_input(self):
        pass
    def test_qcore_run_command(self):
         # check that it is the correct
    #      checking return type
        self.assertTrue(type(qcore_run_command()), str)

    def test_run_qcore(self):
        filename = "/Users/eh19686/Documents/PhD/MNSol_database/subset_water_benzene/benzene/0006nhe.xyz"
        epsilon_out = 2.0
        radial_shift_out = -0.2
        # return stdout

        qcore_output = run_qcore(filename, epsilon_out, radial_shift_out)
        self.assertTrue(json.loads(qcore_output) )

        # return stderr
        epsilon_err = 7.0
        radial_shift_err = "west"
        qcore_err = run_qcore(filename, epsilon_err, radial_shift_err)
        with self.assertRaises(json.JSONDecodeError):
            json.loads(qcore_err)

    def test_qcore_energies(self):
        filename = "/Users/eh19686/Documents/PhD/MNSol_database/subset_water_benzene/benzene/0006nhe.xyz"
        epsilon = 2.0
        radial_shift = -0.2
        return_dict = qcore_energies(filename, epsilon, radial_shift)
        self.assertTrue(type(return_dict), dict)

        expected = {"cosmo_energy": -0.000032218, "gb_energy":-0.000098627}
        subset = {k: v for k, v in return_dict.items() if k in expected}
    # test dict contains -float
        self.assertDictContainsSubset(subset, expected)












    if __name__ == '__main__':
        unittest
