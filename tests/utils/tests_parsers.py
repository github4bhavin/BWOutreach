from utils.parsers import (
    city_parser_from_full_address
)
import pytest

@pytest.mark.parametrize(
    'address,expected',
    [
        ('6321 LAUREN ASHTON AVENUE LAS VEGAS, NV 89131', 'LAS VEGAS')    
    ]
)
def test_city_parser_from_full_address(address, expected):
    result = city_parser_from_full_address(address=address)
    assert result.lower() == expected.lower()
    