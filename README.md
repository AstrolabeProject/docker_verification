# docker_verification

This is the metadata scraping tool used for FITS images in CyVerse/Astrolabe.

Basically, two files need to be adjusted if needed. 
1. ```blank.csv``` holds the cyverse metadata template names
1. ```fits_extract.py``` does the work off extracting the FITS header and populating the csv file. For cards in the FITS header that are not exactly the same as in blank.csv but need to be in the metadata template, add the metadata template name as a key and the FITS header card value as the value of the ```alternatives_dict```dictionary.
