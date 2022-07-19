FROM python:3
ADD req.txt /
RUN pip3 install -r req.txt
ADD s3_downloader.py / 
CMD ["python3","./s3_downloader.py"]

