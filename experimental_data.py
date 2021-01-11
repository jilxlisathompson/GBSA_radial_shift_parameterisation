
import run_qcore
from pandas import read_excel

def get_MNSol_FP():
    global _MNSol_FP

    _MNSol_FP = "/Users/eh19686/Documents/Year1/Solvation_entos/GBSA/MNSolvation_database/analysis/MNSol_alldata.xls"

    return _MNSol_FP


def get_MNSol_data():
    _MNSol_FP = get_MNSol_FP()
    _solvent = run_qcore.get_solvent()

    MNSol_alldata_df = read_excel(open(_MNSol_FP, 'rb'), sheet_name='MNSol')
    MNSol_alldata_df = MNSol_alldata_df.set_index('No.')
    MNSol_df = MNSol_alldata_df[MNSol_alldata_df['Solvent'] == _solvent]
    MNSol_df = MNSol_df[MNSol_df['Charge'] == 0]

    global _epsilon
    _epsilon = MNSol_df['eps'].values[0]


    return _epsilon, MNSol_df