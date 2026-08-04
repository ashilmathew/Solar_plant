from pydantic import BaseModel


class ReportSummary(BaseModel):
    total_energy: float
    average_power: float
    maximum_power: float
    minimum_power: float
    average_voltage: float
    average_current: float


class ReportResponse(BaseModel):
    device_name: str
    from_date: str
    to_date: str
    summary: ReportSummary