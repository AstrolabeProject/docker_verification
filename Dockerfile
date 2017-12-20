FROM python:2.7-slim
ADD fits_extract.py /
ADD cvnidwabcut.fits /
ADD cvnidwafcut.fits /
ADD blank.csv /
RUN pip install astropy
ENTRYPOINT [ "python", "./fits_extract.py" ]