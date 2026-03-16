import pytest
import numpy as np

from assignment_8 import analyze_image


@pytest.mark.parametrize(
    ("pac_num",),
    [(0,),
     (1,),
     (2,),
     ])

def test_read_data(pac_num):

    image_true = np.load('pomocna_slozka_pro_testy/image' + str(pac_num) + '.npy')

    mask, fraction, mean_intensity = analyze_image(image_true)

    mask_true = np.load('pomocna_slozka_pro_testy/mask' + str(pac_num) + '.npy')
    fraction_true = np.load('pomocna_slozka_pro_testy/fraction' + str(pac_num) + '.npy')
    mean_intensity_true = np.load('pomocna_slozka_pro_testy/mean_intensity' + str(pac_num) + '.npy')


    assert (mask == mask_true).all()
    assert fraction == fraction_true
    assert mean_intensity == mean_intensity_true