from typing import Optional

from pydantic import BaseModel, EmailStr, Field


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
    id: str = Field(alias="id")

    model_config = {
        "populate_by_name": True
    }