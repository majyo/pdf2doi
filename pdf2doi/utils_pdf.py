from collections.abc import Callable
from io import StringIO
from typing import cast, BinaryIO

from PyPDF2 import PdfFileReader
from pdfminer.converter import TextConverter
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.pdfpage import PDFPage
from pdfminer.utils import open_filename


def cutoff_ref_pages_for_pypdf(pdf_file: str, ref_judging_func: Callable[[str], bool] = None,
                               fallback_cutoff_ratio: float = 0.5) -> int:
    pdf: PdfFileReader = PdfFileReader(pdf_file, strict=False)
    page_count = pdf.getNumPages()
    if page_count == 0:
        return 0
    if ref_judging_func is None:
        return int(page_count * fallback_cutoff_ratio)
    for i in range(page_count):
        page = pdf.getPage(i)
        text = page.extract_text()
        if text is None or not text.strip():
            continue
        if ref_judging_func(text):
            return i
    return int(page_count * fallback_cutoff_ratio)


def cutoff_ref_pages_for_pdfminer(pdf_file: str, ref_judging_func: Callable[[str], bool] = None,
                               fallback_cutoff_ratio: float = 0.5) -> int:
    with open_filename(pdf_file, "rb") as fp, StringIO() as output_string:
        fp = cast(BinaryIO, fp)  # we opened in binary mode
        rsrcmgr = PDFResourceManager(caching=True)
        device = TextConverter(rsrcmgr, output_string, codec="utf-8", laparams=None)
        interpreter = PDFPageInterpreter(rsrcmgr, device)
        pages = PDFPage.get_pages(fp)

        for i, page in enumerate(pages):
            interpreter.process_page(page)
            output_string.flush()
            page_content = output_string.read()
            if not page_content.strip():
                continue
            if ref_judging_func and ref_judging_func(page_content):
                return i
        page_count = i
        return int(page_count * fallback_cutoff_ratio)
