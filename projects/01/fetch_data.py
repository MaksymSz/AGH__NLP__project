import requests
from pathlib import Path
import os
import gzip

datapath = Path('../../data/')

base_url = "https://clarin.eurac.edu/repository/xmlui/bitstream/handle/20.500.12124/3"

# List of file names to download
file_names = [
    "paisa.raw.utf8.gz",
    "paisa.annotated.CoNLL.utf8.gz",
]

for file_name in file_names:
    if not os.path.exists(datapath / file_name):
        file_url = f'{base_url}/{file_name}'
        response = requests.get(file_url)

        if response.status_code == 200:
            with open(datapath / file_name, mode='wb') as f:
                f.write(response.content)
            print(f'Downloaded {file_name}')
        else:
            print(f'Failed to download {file_name} (Status code: {response.status_code})')

if not os.path.exists(datapath / 'corpus_raw.txt'):
    with gzip.open(datapath / 'paisa.raw.utf8.gz', 'rt', encoding='utf-8') as f:
        content = f.read()
    with open(datapath / 'corpus_raw.txt', 'a', encoding='utf-8') as txt:
        txt.write(content)
