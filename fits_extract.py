import sys
import warnings
from astropy.io import fits


def extract_fits(file):
    """Check if file is fits standard.

    If it is, output csv file with header. Else, output that it is not in a log file.
    """
    alternates_dict = {
        'spatial_axis_1_number_bins': 'NAXIS1',
        'spatial_axis_2_number_bins': 'NAXIS2',
        'start_time': 'DATE-OBS',
        'facility_name': 'INSTRUME',
        'instrument_name': 'TELESCOP',
        'obs_creator_name': 'OBSERVER',
        'obs_title': 'OBJECT'
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
                            if key == 'CRVAL1':
                                if 'RA' in header['CTYPE1']:
                                    headers.write(str(f[0].header['right_ascension']) + ',')
                                elif 'DEC' in header['CTYPE1']:
                                    headers.write(str(f[0].header['declination']) + ',')
                                else:
                                    log.write("Warning: CTYPE {} not yet supported".format(header['CTYPE1']))
                                    headers.write(',')
                            if key == 'CRVAL2':
                                if 'RA' in header['CTYPE2']:
                                    headers.write(str(f[0].header['right_ascension']) + ',')
                                elif 'DEC' in header['CTYPE2']:
                                    headers.write(str(f[0].header['declination']) + ',')
                                else:
                                    log.write("Warning: CTYPE {} not yet supported".format(header['CTYPE2']))
                                    headers.write(',')
                            headers.write(str(f[0].header[key]) + ',')
                    except KeyError:
                        headers.write(',')

if __name__ == '__main__':
    extract_fits(sys.argv[1])
