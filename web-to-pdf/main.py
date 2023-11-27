from pdf_converter import PdfConverter

if __name__ == '__main__':
    is_converted = PdfConverter.from_url(
        url="https://generativeai.pub/building-a-streamlit-q-a-app-using-openais-assistant-api-8193f718e7ed",
        output_path="outputs/medium-2.pdf",
        options={'orientation': "Landscape"})
    print('Conversion status:', is_converted)
