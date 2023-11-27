class PdfConverter:
    @staticmethod
    def from_url(url, output_path):
        from pdfkit import from_url
        return from_url(url=url, output_path=output_path)
