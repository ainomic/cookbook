from typing import Any, Dict


class PdfConverter:
    _options = {
        'encoding': "UTF-8",
        'no-outline': None,
        # 'orientation': 'Landscape',
        # 'page-size': 'Letter',
        # 'margin-top': '0.75in',
        # 'margin-right': '0.75in',
        # 'margin-bottom': '0.75in',
        # 'margin-left': '0.75in',
        # 'custom-header': [
        #     ('Accept-Encoding', 'gzip')
        # ],
        # 'cookie': [
        #     ('cookie-empty-value', '""')
        #     ('cookie-name1', 'cookie-value1'),
        #     ('cookie-name2', 'cookie-value2'),
        # ],
    }

    @staticmethod
    def from_url(url, output_path, options: Dict[str, Any] = None):
        from pdfkit import from_url
        final_options = PdfConverter._options.copy()
        if options:
            final_options.update(options)
        return from_url(
            url=url,
            output_path=output_path,
            options=final_options,
        )
