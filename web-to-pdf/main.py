import pdfkit

pdf = pdfkit.from_url(
    url='https://weasyprint.org/', output_path="weasyprint.pdf")
print("Result:", pdf)
