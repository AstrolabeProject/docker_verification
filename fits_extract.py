import sys
import warnings
from astropy.io import fits


def extract_fits(file):
    """Check if file is fits standard.

    If it is, output csv file with header. Else, output that it is not in a log file.
    """
    alternates_dict = {
        'right_ascension': 'CRVAL1',
        'declination': 'CRVAL2',
        'spatial_axis_1_number_bins': 'NAXIS1',
        'spatial_axis_2_number_bins': 'NAXIS2',
        'start_time': 'DATE-OBS',
    }
    f = fits.open(file)
    print(file)
    with warnings.catch_warnings(record=True) as w:
        f.verify()
        if len(w) > 0:
            log = open('log.txt', 'w')
            log.write("The file {} does not meet fits standard.".format(file))
        else:
            with open(file[:-5] + '.csv', 'w') as headers:
                template = open('/blank.csv', 'r').readlines()[0]
                headers.write(template)
                for key in template[:-1].split(','):
                    try:
                        if key == 'file name or path':
                            headers.write(file + ',')
                        elif key in alternates_dict.keys():
                            headers.write(str(f[0].header[alternates_dict[key]]) + ',')
                        else:
                            headers.write(str(f[0].header[key]) + ',')
                    except KeyError:
                        headers.write(',')
               
if __name__ == '__main__':
    extract_fits(sys.argv[1])
