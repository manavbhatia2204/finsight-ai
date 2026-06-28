from io import BytesIO

from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import Paragraph, SimpleDocTemplate


def generate_pdf(
    prediction: dict,
    history: dict,
    report: str,
):
    """
    Generate PDF report.
    """

    buffer = BytesIO()

    doc = SimpleDocTemplate(buffer)

    styles = getSampleStyleSheet()

    elements = []

    elements.append(
        Paragraph(
            "<b>FinSight AI Report</b>",
            styles["Title"],
        )
    )

    elements.append(
        Paragraph(
            f"<b>Ticker:</b> {prediction['ticker']}",
            styles["BodyText"],
        )
    )

    elements.append(
        Paragraph(
            f"<b>Prediction:</b> {prediction['prediction']}",
            styles["BodyText"],
        )
    )

    confidence = max(
        prediction["confidence_up"],
        prediction["confidence_down"],
    )

    elements.append(
        Paragraph(
            f"<b>Confidence:</b> {confidence:.2f}%",
            styles["BodyText"],
        )
    )

    latest = history["records"][0]

    elements.append(
        Paragraph(
            f"<b>Latest Close:</b> ${latest['close']:.2f}",
            styles["BodyText"],
        )
    )

    elements.append(
        Paragraph(
            "<br/><b>AI Research</b>",
            styles["Heading2"],
        )
    )

    elements.append(
        Paragraph(
            report.replace("\n", "<br/>"),
            styles["BodyText"],
        )
    )

    doc.build(elements)

    buffer.seek(0)

    return buffer