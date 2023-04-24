# extract all zips to the ex folder

import os
import zipfile


def extract_zip(zip_file, extract_dir):
    zip_ref = zipfile.ZipFile(zip_file, 'r')
    zip_ref.extractall(extract_dir)
    zip_ref.close()


def main():
    dir = input('Enter the directory: ')
    os.chdir(dir)
    # order to the creation date
    # for i, file in enumerate(sorted(os.listdir(dir), key=os.path.getctime)):
    # sort by creation date
    for i, file in enumerate(sorted(os.listdir(dir), key=os.path.getmtime)):
        # if exercises folder doesn't exist, create
        if not os.path.exists('exercises'):
            os.mkdir('exercises')

        # create a folder for each zip that named as order number
        # extract to the new folder
        if file.__contains__('.zip'):
            os.mkdir('exercises/' + str(i))
            extract_zip(file, 'exercises/' + str(i))
            print('Extracted ' + file + ' to ' + 'exercises/' + str(i))


if __name__ == '__main__':
    main()
