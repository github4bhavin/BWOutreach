
import logging

from pydantic import Field, field_validator, BaseModel
from pydantic.dataclasses import dataclass
from datetime import date, datetime

from src.source_base import SourceBase
from src.Targets.outreach_target import OutreachTarget

from utils.parsers import (
    city_parser_from_full_address
)

class S1(BaseModel):
    name :str = Field(alias='Name')
    credential_type :str = Field(alias='Credential Type')
    credential_number :str = Field(alias='Credential Number')
    status :str = Field(alias='Status')
    expiration_date :date = Field(alias='Expiration Date')
    disciplinary_action :str = Field('Disciplinary Action', max_length=1)
    address :str = Field(alias='Address')
    state :str = Field(alias='State')
    county :str = Field(alias='County')
    phone :str = Field(alias='Phone')
    first_issue_date :date = Field(alias='First Issue Date')
    primary_contact_name :str = Field(alias='Primary Contact Name')
    primary_contact_role :str = Field(alias='Primary Contact Role')
    
    @field_validator('county')
    def validate_county(cls, v:str) ->str:
        return v.lower()
    
    @property
    def address1(self) -> str:
        return self.address.lower()
    
    @property
    def licensee_name(self) -> str:
        return self.primary_contact_name.lower()

    @property
    def license_type(self) -> str:
        return self.credential_type.lower()

    @property
    def license_number(self) -> str:
        return self.credential_number

    @property
    def license_issued(self) -> date:
        return self.first_issue_date

    @property
    def license_status(self) -> str:
        return 'expired' if self.expiration_date < date.today() else 'active'
    
    @property
    def first_name(self) -> str:
        return self.primary_contact_name.split(' ')[0].capitalize()
    
    @property
    def last_name(self) -> str:
        return self.primary_contact_name.split(' ')[1].capitalize()
    
    @property
    def company(self) -> str:
        return self.name.lower()
    
    @property
    def city(self) -> str:
        return city_parser_from_full_address(address=self.address).lower()
    
    @property
    def certificate_expiration_date(self) -> date:
        return self.expiration_date
    
    def get_outreach_obj(self) -> OutreachTarget:
        print(self.dict())
        print(self.certificate_expiration_date)
        return OutreachTarget(
            **{
               field_name : getattr(self, field_name) \
                   for field_name, field in OutreachTarget().model_fields.items() \
                       if hasattr(self, field_name)
            }
        )
    