import pytest
import numpy as np

from assignment_8 import analyze_signal


@pytest.mark.parametrize(
    ("pac_num",),
    [(0,),
     (1,),
     (2,),
     ])

def test_read_data(pac_num):

    signal_true = np.load('pomocna_slozka_pro_testy/signal' + str(pac_num) + '.npy')

    detekce, tep = analyze_signal(signal_true)

    detekce_true = np.load('pomocna_slozka_pro_testy/detekce' + str(pac_num) + '.npy')
    tep_true = np.load('pomocna_slozka_pro_testy/tep' + str(pac_num) + '.npy')



    assert (detekce == detekce_true).all()
    assert tep == tep_true