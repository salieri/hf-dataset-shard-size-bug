## 1. Setup

```bash
python3 -m venv ./venv
. ./venv/bin/activate
pip install -r requirements.txt
```


## 2. Generate images for the dataset

Note: This will generate a ~10GB dataset locally.

```bash
python3 generate.py
```


## 3. Create dataset & upload to Huggingface

```bash
export HF_REPO=username/dataset  # <-- specify here where to upload
python3 upload.py
```
