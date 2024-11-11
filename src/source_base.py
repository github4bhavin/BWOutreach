
from pydantic import BaseModel
from abc import ABC, abstractmethod

from src.Targets.outreach_target import OutreachTarget

class SourceBase(BaseModel):
    
    @abstractmethod
    def get_outreach_obj(self) -> OutreachTarget:
        pass
