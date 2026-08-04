from fastapi import APIRouter
from fastapi.responses import Response

from app.schemas.reports import ReportResponse
from app.services.reports_service import ReportsService

router = APIRouter(
    prefix="/reports",
    tags=["Reports"],
)

service = ReportsService()


@router.get(
    "/device/{device_id}",
    response_model=ReportResponse,
)
async def get_report(device_id: str):
    """
    Generate report summary for a device.
    """
    return await service.generate_report(device_id)


@router.get("/device/{device_id}/csv")
async def download_csv(device_id: str):
    """
    Download report as CSV.
    """
    csv_data = await service.generate_csv(device_id)

    return Response(
        content=csv_data,
        media_type="text/csv",
        headers={
            "Content-Disposition": f"attachment; filename={device_id}_report.csv"
        },
    )


@router.get("/device/{device_id}/pdf")
async def download_pdf(device_id: str):
    """
    Download report as PDF.
    """
    pdf_data = await service.generate_pdf(device_id)

    return Response(
        content=pdf_data,
        media_type="application/pdf",
        headers={
            "Content-Disposition": f"attachment; filename={device_id}_report.pdf"
        },
    )