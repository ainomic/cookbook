# Webpage to PDF

You can convert any website to a PDF file which can be further used for downstream tasks.

## Setup dev environment

1. Install `wkhtmltopdf`
   1. MacOS: `brew install Caskroom/cask/wkhtmltopdf`
1. Create virtual environment: `conda create -n web-to-pdf-env -y python=3.10`
1. Activate virtual environment: `conda activate web-to-pdf-env`
1. Install dependencies: `pip install -r requirements.txt`
