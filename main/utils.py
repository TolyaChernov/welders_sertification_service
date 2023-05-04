import os
from io import BytesIO

from django.http import HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa

from ptm import settings


def render_to_pdf(url_template: str, contexto: dict ={}):
    template = get_template(url_template)
    html = template.render(contexto)
    result = BytesIO()
    pdf = pisa.pisaDocument(
        BytesIO(html.encode("UTF-16")),
        result,
        encoding="utf-8",
        link_callback=fetch_pdf_resources,
    )
    if not pdf.err:
        return HttpResponse(result.getvalue(), content_type="application/pdf")
    return None


def fetch_pdf_resources(uri: str, rel: str):
    """
    Description of fetch_pdf_resources

    Args:
        uri (str):
        rel (str):

    """
    if uri.find(settings.MEDIA_URL) != -1:
        path = os.path.join(
            settings.MEDIA_ROOT, uri.replace(
                settings.MEDIA_URL, ""))
    elif uri.find(settings.STATIC_URL) != -1:
        path = os.path.join(
            settings.STATIC_ROOT, uri.replace(
                settings.STATIC_URL, ""))

    else:
        path = None
    return path
