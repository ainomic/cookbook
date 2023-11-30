# Blog generation

Generate blog from the specific context as documents uploaded.

## Setup Dev environment

1. Create virtual environment: `conda create -n blog-gen-env -y python=3.10`
1. Activate virtual environment: `conda activate blog-gen-env`
1. Install dependencies: `pip install -r requirements.txt`
1. Rename `.env.example` to `.env` and update the values of environment variables.

## Run the application

1. Run: `streamlit run app.py`
1. Upload a PDF file
1. Click `Generate blog` button
1. Wait to see your generated blog in 2-3 minutes
