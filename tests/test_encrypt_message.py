import pytest
from challenges.challenge_encrypt_message import encrypt_message


def test_encrypt_message():
    assert encrypt_message('pipoca', 3) == 'pip_aco'

    assert encrypt_message('pipoca', 2) == 'acop_ip'

    with pytest.raises(TypeError, match='tipo inválido'):
        encrypt_message('pipoca', '3')

    with pytest.raises(TypeError, match='tipo inválido para message'):
        encrypt_message(2, 3)
