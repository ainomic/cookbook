# QnA with Document

This application enables user to query through uploaded document and receive answer based on the relevant information in the document. It uses open source models and libraries.

## Setup dev environment

1. Create virtual environment: `conda create -n os-pdf-qa-env -y python=3.10`
1. Activate environment: `conda activate os-pdf-qa-env`
1. Install dependencies: `pip install -r requirements.txt`
1. Create dir: `mkdir -p models`
1. Download the model param file: `huggingface-cli download TheBloke/zephyr-7B-beta-GGUF zephyr-7b-beta.Q4_K_M.gguf --local-dir ./models --local-dir-use-symlinks False`
