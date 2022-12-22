import os

hf_repo = os.environ.get('HF_REPO', 'username/somerepo')

num_samples = int(os.environ.get('NUM_SAMPLES', '1000'))
sample_source_path = os.environ.get('SOURCE_PATH', './source-images')
output_path = os.environ.get('OUTPUT_PATH', './output')

metadata_file = os.path.join(output_path, 'metadata.jsonl')
source_files = os.listdir(sample_source_path)
