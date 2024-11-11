import pytest
from datetime import datetime, date
from dateutil import parser
from src.Sources.S1 import S1

from pprint import pprint

@pytest.mark.parametrize(
'input_record,expected',
[
    (
        {
            'Name': "DEE'S PLAY & LEARN CHRISTIAN ACADEMY",
            'Credential Type': 'GROUP CARE',
            'Credential Number': '2454-23',
            'Status': 'Active',
            'Expiration Date': parser.parse('2024-06-30 00:00:00').date(),
            'Disciplinary Action': 'N',
            'Address': '6321 LAUREN ASHTON AVENUE LAS VEGAS, NV 89131',
            'State': 'NV',
            'County': 'CLARK',
            'Phone': '510-551-5129',
            'First Issue Date': parser.parse('2018-07-09 00:00:00').date(),
            'Primary Contact Name': 'DEETRA STEWART',
            'Primary Contact Role': 'Owner'
        },
        {
            'accepts_financial_aid': None,
            'address1': '6321 LAUREN ASHTON AVENUE LAS VEGAS, NV 89131'.lower(),
            'address2': None,
            'ages_served': None,
            'capacity': None,
            'certificate_expiration_date': parser.parse('2024-06-30 00:00:00').date(),
            'city': 'las vegas',
            'company': "DEE'S PLAY & LEARN CHRISTIAN ACADEMY".lower(),
            'county': 'CLARK'.lower(),
            'curriculum_type': None,
            'email': None,
            'facility_type': None,
            'first_name': 'Deetra',
            'language': None,
            'last_name': "Stewart",
            'license_issued': parser.parse('2018-07-09 00:00:00').date(),
            'license_number': '2454-23',
            'license_renewed': None,
            'license_status': 'expired',
            'license_type': 'GROUP CARE'.lower(),
            'licensee_name': 'deetra stewart',
            'max_age': None,
            'min_age': None,
            'operator': None,
            'phone': '510-551-5129',
            'phone2': None,
            'provider_id': None,
            'schedule': None,
            'state': 'NV',
            'title': None,
            'website_address': None,
            'zip': None
        }
    )
])
def test_outreach_target_mapping_for_source(input_record :dict, expected:dict):
    s1 = S1(**input_record)
    outreach_obj = s1.get_outreach_obj()
    pprint(input_record)
    pprint(outreach_obj.dict())
    assert expected == outreach_obj.dict()
    