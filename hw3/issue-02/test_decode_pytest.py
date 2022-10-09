import pytest
from morse import decode


@pytest.mark.parametrize(
    'morse, eng', [
        ('', ''),
        ('... --- ...', 'SOS'),
        ('.-- .- --. --- -.', 'WAGON')
    ]
)
def test_simple_strings(morse: str, eng: str):
    assert decode(morse) == eng


@pytest.mark.parametrize(
    'morse, eng', [
        (123, '')
    ]
)
def test_wrong_input(morse: str, eng: str):
    with pytest.raises(AttributeError):
        decode(morse)


@pytest.mark.parametrize(
    'morse, eng', [
        ('.-- .... ---   ... .--. -.--', 'WHO SPY')
    ]
)
def test_sentence(morse: str, eng: str):
    assert decode(morse) == eng
