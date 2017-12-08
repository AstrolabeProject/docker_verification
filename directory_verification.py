import os
import sys
import warnings
from astropy.io import fits
def scan_directory(directory):
    valid = []
    invalid = []
    already_have_file = []
    for file in os.listdir(directory):
        if file.endswith(".fits"):
            if os.path.isfile(file[:-5] + '.csv'):
                already_have_file.append(file) 
                continue
            f = fits.open(directory + '/' + file)
            with warnings.catch_warnings(record=True) as w:
                f.verify()
                if len(w) > 0:
                    invalid.append(file)
                    continue
                else:
                    valid.append(file)
                    with open(file[:-5] + '.csv', 'w') as headers:
                        headers.write("name, value, description \n")
                        for key in f[0].header._cards:
                                headers.write('{}, {}, {} \n'.format(key[0], str(key[1]).replace(",",""), key[2]))
    os.remove('log.txt')
    log = open('log.txt', 'w')
    log.write("The following files meet FITS standard: \n \n")
    for i in valid:
        log.write(i + "\n")
    log.write("\n \nThe following files do not meet fits standard: \n \n")
    for i in invalid:
        log.write(i + "\n")
    log.write("\n \nThe following files were skipped: \n \n")
    for i in already_have_file:
        log.write(i + "\n")
    log.write('\n \nIf your files do not meet fits standard, you may edit them with your program of choice or use our web service: www.website.com')

if __name__ == '__main__':
    print('functional')
    print('here is the argv')
    print(sys.argv[1])
    print('-----')
    print(os.getcwd())
    os.listdir(os.getcwd())
    print('---')
    print('-----')
    scan_directory(sys.argv[1])