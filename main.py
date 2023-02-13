# extract all zips to the ex folder

import os
import zipfile

def extract_zip(zip_file, extract_dir):
    zip_ref = zipfile.ZipFile(zip_file, 'r')
    zip_ref.extractall(extract_dir)
    zip_ref.close()

def main():
    for f in os.listdir('.'):
        if f.endswith('.zip'):
            extract_zip(f, 'ex')

if __name__ == '__main__':
    main()
    