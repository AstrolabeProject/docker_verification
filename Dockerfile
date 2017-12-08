FROM python:3
ADD directory_verification.py /
COPY Hunter /
RUN pip install astropy
CMD [ "python", "./directory_verification.py" ]