from pydantic import BaseModel, IPvAnyAddress

class MonitorCreate(BaseModel):
    ip: IPvAnyAddress
