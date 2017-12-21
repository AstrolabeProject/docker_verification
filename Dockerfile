FROM python:2.7-slim
ADD https://raw.githubusercontent.com/endere/docker_verification/master/fits_extract.py /
ADD https://raw.githubusercontent.com/endere/docker_verification/master/blank.csv /
ADD cvnidwafcut.fits /
ADD cvnidwabcut.fits /
RUN pip install astropy
ENTRYPOINT [ "python", "/fits_extract.py" ]

