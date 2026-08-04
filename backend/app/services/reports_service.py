import csv
import io

from fastapi import HTTPException, status

from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import Paragraph, SimpleDocTemplate

from app.repositories.reports_repository import ReportsRepository


class ReportsService:

    def __init__(self):
        self.repository = ReportsRepository()

    async def generate_report(self, device_id: str):

        device = await self.repository.get_device(device_id)

        if not device:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Device not found",
            )

        telemetry = await self.repository.get_report_data(device_id)

        if not telemetry:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="No telemetry available",
            )

        powers = []
        voltages = []
        currents = []
        temperatures = []

        for item in telemetry:

            electrical = item.get("electrical", {})
            environment = item.get("environment", {})

            powers.append(electrical.get("power", 0))
            voltages.append(electrical.get("voltage", 0))
            currents.append(electrical.get("current", 0))
            temperatures.append(environment.get("temperature", 0))

        latest = telemetry[-1]

        report = {
            "device_name": device["name"],
            "from_date": str(telemetry[0]["timestamp"]),
            "to_date": str(telemetry[-1]["timestamp"]),
            "summary": {
                "total_energy": latest["energy"]["total"],
                "average_power": round(sum(powers) / len(powers), 2),
                "maximum_power": max(powers),
                "minimum_power": min(powers),
                "average_voltage": round(sum(voltages) / len(voltages), 2),
                "average_current": round(sum(currents) / len(currents), 2),
                "average_temperature": round(
                    sum(temperatures) / len(temperatures), 2
                ),
            },
        }

        return report

    async def generate_csv(self, device_id: str):

        telemetry = await self.repository.get_report_data(device_id)

        if not telemetry:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="No telemetry available",
            )

        csv_buffer = io.StringIO()

        writer = csv.writer(csv_buffer)

        writer.writerow([
            "Timestamp",
            "Voltage",
            "Current",
            "Frequency",
            "Power",
            "Power Factor",
            "Today's Energy",
            "Total Energy",
            "Temperature",
            "Humidity",
            "Status",
        ])

        for item in telemetry:

            writer.writerow([
                item["timestamp"],
                item["electrical"]["voltage"],
                item["electrical"]["current"],
                item["electrical"]["frequency"],
                item["electrical"]["power"],
                item["electrical"]["power_factor"],
                item["energy"]["today"],
                item["energy"]["total"],
                item["environment"]["temperature"],
                item["environment"]["humidity"],
                item["status"],
            ])

        return csv_buffer.getvalue()

    async def generate_pdf(self, device_id: str):

        report = await self.generate_report(device_id)

        buffer = io.BytesIO()

        document = SimpleDocTemplate(buffer)

        styles = getSampleStyleSheet()

        story = []

        story.append(
            Paragraph(
                "Solar Plant Monitoring Report",
                styles["Title"],
            )
        )

        story.append(
            Paragraph(
                f"<b>Device:</b> {report['device_name']}",
                styles["Normal"],
            )
        )

        story.append(
            Paragraph(
                f"<b>From:</b> {report['from_date']}",
                styles["Normal"],
            )
        )

        story.append(
            Paragraph(
                f"<b>To:</b> {report['to_date']}",
                styles["Normal"],
            )
        )

        story.append(
            Paragraph("<br/>", styles["Normal"])
        )

        story.append(
            Paragraph(
                "<b>Summary</b>",
                styles["Heading2"],
            )
        )

        summary = report["summary"]

        for key, value in summary.items():

            story.append(
                Paragraph(
                    f"{key.replace('_', ' ').title()}: {value}",
                    styles["Normal"],
                )
            )

        document.build(story)

        pdf = buffer.getvalue()

        buffer.close()

        return pdf