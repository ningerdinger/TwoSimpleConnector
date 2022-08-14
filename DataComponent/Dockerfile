FROM python:3.9 
# Or any preferred Python version.
ADD WritingToDB.py .
ADD CBS.py .

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt
CMD [“python”, “./CBS.py”] 
# Or enter the name of your unique directory and parameter set.