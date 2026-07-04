from pydantic import BaseModel,Field
from typing import Any
class Health(BaseModel): service:str; status:str="ok"; version:str="2.0.0"
class MapPoint(BaseModel): id:str; lat:float; lon:float; title:str; category:str; properties:dict[str,Any]=Field(default_factory=dict)
