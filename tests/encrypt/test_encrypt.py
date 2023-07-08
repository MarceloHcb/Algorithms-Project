import pytest
from challenges.challenge_encrypt_message import encrypt_message


def test_encrypt_message():
    assert encrypt_message('Python', 1) == 'P_nohty'
    assert encrypt_message('Python', 2) == 'noht_yP'
    assert encrypt_message('Python', 3) == 'tyP_noh'
    assert encrypt_message('Python', 4) == 'no_htyP'
    assert encrypt_message('Python', 5) == 'ohtyP_n'
    assert encrypt_message('Python', 6) == 'nohtyP'
    assert encrypt_message('Python', 9) == 'nohtyP'
    with pytest.raises(TypeError):
        encrypt_message(3, '1')
