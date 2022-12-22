import json
import os
import datasets

from config import output_path, metadata_file, hf_repo

print(f'uploading dataset {output_path} to {hf_repo}')

def load_from_metadata_jsonl(filename):
    with open(filename, 'rt') as jsonl_file:
        for line in jsonl_file:
            record = json.loads(line)
            fn = os.path.join(output_path, record['file_name'])
            data = {'image': fn, 'text': record['text']}
            yield data

ds = datasets.Dataset.from_generator(
  load_from_metadata_jsonl,
  features=datasets.Features(
    {
      "image": datasets.Image(),
      "text": datasets.Value(dtype='string', id=None)
    }
  ),
  gen_kwargs={'filename': metadata_file},
)

ds.cast_column('image', datasets.Image())

# max_shard_size must be < 2GB, or you will run into problems
ds.push_to_hub(hf_repo, private=True, embed_external_files=True, max_shard_size='75MB')

print('done')
