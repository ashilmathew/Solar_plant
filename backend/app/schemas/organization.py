from typing import Optional

from pydantic import BaseModel, ConfigDict, EmailStr


class OrganizationBase(BaseModel):
    name: str
    address: Optional[str] = None
    email: Optional[EmailStr] = None
    phone: Optional[str] = None
    logo: Optional[str] = None
    status: str = "ACTIVE"


class OrganizationCreate(OrganizationBase):
    pass


class OrganizationUpdate(BaseModel):
    name: Optional[str] = None
    address: Optional[str] = None
    email: Optional[EmailStr] = None
    phone: Optional[str] = None
    logo: Optional[str] = None
    status: Optional[str] = None


class OrganizationResponse(OrganizationBase):
    id: int

    model_config = ConfigDict(from_attributes=True)