import pytest
import numpy as np

from assignment_8 import read_data


@pytest.mark.parametrize(
    ("pac_num",),
    [(0,),
     (1,),
     (2,),
     ])

def test_read_data(pac_num):
    image, signal = read_data(pac_num)

    image_true = np.load('pomocna_slozka_pro_testy/image' + str(pac_num) + '.npy')
    signal_true = np.load('pomocna_slozka_pro_testy/signal' + str(pac_num) + '.npy')

    assert (image_true == image).all()
    assert (signal_true == signal).all()