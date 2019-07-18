FROM python:3.7.4
RUN pip install fastparquet pandas
COPY test_fastparquet.py .
CMD python test_fastparquet.py