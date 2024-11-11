
from pydantic import BaseModel, Field
from datetime import datetime, date
from typing import Optional

class OutreachTarget(BaseModel):
    """
    only phone + address cannot be null according to problem statement
    """
    
    accepts_financial_aid :Optional[str] = None
    ages_served :Optional[str] = None
    capacity :Optional[int] = None
    certificate_expiration_date : Optional[date] = None
    city :Optional[str] = None
    address1 :Optional[str] = None 
    address2 :Optional[str] = None
    company :Optional[str] = None
    phone :Optional[str] = None 
    phone2 :Optional[str] = None
    county :Optional[str] = None
    curriculum_type :Optional[str] = None
    email :Optional[str] = None
    first_name :Optional[str] = None
    language :Optional[str] = None
    last_name :Optional[str] = None
    license_status :Optional[str] = None
    license_issued :Optional[date] = None
    license_number :Optional[str] = None
    license_renewed : Optional[date] = None
    license_type :Optional[str] = None
    licensee_name :Optional[str] = None
    max_age :Optional[str] = None
    min_age :Optional[str] = None
    operator :Optional[str] = None
    provider_id :Optional[str] = None
    schedule :Optional[str] = None
    state :Optional[str] = None
    title :Optional[str] = None
    website_address :Optional[str] = None
    zip :Optional[str] = None
    facility_type :str = None
    
    