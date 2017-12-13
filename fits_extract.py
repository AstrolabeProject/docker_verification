import sys
import warnings
from astropy.io import fits


def extract_fits(file):
    """Check if file is fits standard.

    If it is, output csv file with header. Else, output that it is not in a log file.
    """
    f = fits.open(file)
    with warnings.catch_warnings(record=True) as w:
        f.verify()
        if len(w) > 0:
            log = open('log.txt', 'w')
            log.write("The file {} does not meet fits standard.".format(file))
        else:
            with open(file[:-5] + '.csv', 'w') as headers:
                headers.write("name, value, description \n")
                for key in f[0].header._cards:
                        headers.write('{}, {}, {} \n'.format(key[0], str(key[1]).replace(",",""), key[2]))

if __name__ == '__main__':
    extract_fits(sys.argv[1])
