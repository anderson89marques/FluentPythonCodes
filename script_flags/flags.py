import os
import time
import sys

import requests
from tqdm import tqdm

POP20_CC = 'CN IN US ID BR PK NG BD RU JP MX PH VN ET EG DE IR TR CD FR'.split()
BASE_URL = 'http://flupy.org/data/flags'
DEST_DIR = 'downloads/'

def save_flag(img, filename):
    path = os.path.join(DEST_DIR, filename)
    with open(path, 'wb') as fp:
        fp.write(img)

def get_flag(cc):
    url = f'{BASE_URL}/{cc.lower()}/{cc.lower()}.gif'
    resp = requests.get(url)
    return resp.content

def show(text):
    print(text, end=' ')
    # É necessário pois o python epsera uma quebra de linha para descarregar o buffer stdout
    sys.stdout.flush()

def download_many(cc_list):
    cc_iter = sorted(cc_list)
    cc_iter = tqdm(cc_iter)  # Para exibir barra de progresso animada no console
    for cc in cc_iter:
        image = get_flag(cc)
        show(cc)
        save_flag(image, cc)
    
    return len(cc_list)

def main(download_many):
    t0 = time.time()
    count = download_many(POP20_CC)
    elapsed = time.time() - t0
    print(f'\n{count} flags downloaded in {elapsed:.2f}')

if __name__ == '__main__':
    main(download_many)