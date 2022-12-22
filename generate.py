import os
import random
import pathlib
import shutil
import json

from config import num_samples, sample_source_path, output_path, metadata_file, source_files

random.seed(0)
os.makedirs(output_path, exist_ok=True)

print(f'Generating {num_samples} samples into {output_path}')

with open(metadata_file, 'wt') as meta:
    for i in range(num_samples):
        if i % 100 == 0:
            print(f'    {i}/{num_samples}...')

        source_file = random.choice(source_files)
        ext = pathlib.Path(source_file).suffix

        fn = str(i).rjust(8, '0')
        sub_path = os.path.join(fn[-4], fn[-3], fn[-2], fn[-1])

        fn_relative = os.path.join('generated', sub_path, f'{fn}{ext}')
        fn_absolute = os.path.join(output_path, fn_relative)

        os.makedirs(os.path.dirname(fn_absolute), exist_ok=True)

        shutil.copyfile(os.path.join(sample_source_path, source_file), fn_absolute)

        meta.write(json.dumps({'file_name': fn_relative, 'text': f'hello world {i}'}) + '\n')
