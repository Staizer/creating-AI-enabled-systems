FROM python:3.8
COPY . ./
RUN pip3 install -r requirements.txt
CMD ["Bryson_NLP_Module4.py"]
ENTRYPOINT ["python"]