FROM python:3.7
ENV PYTHONUNBUFFERED 1

RUN apt-get --fix-missing update && apt-get --fix-broken install && apt-get install -y poppler-utils && apt-get install -y tesseract-ocr && \
    apt-get install -y libtesseract-dev && apt-get install -y libleptonica-dev && ldconfig && apt-get install -y python3.7 && \
    apt-get install -y python3-pip && apt-get install -y ffmpeg libsm6 libxext6
RUN apt-get --fix-missing update && apt-get install -y tesseract-ocr-rus


RUN mkdir /web_fine_OCR

WORKDIR /web_fine_OCR
#ADD requirements.txt ./docker/
COPY . .
RUN ls -l
RUN pip install --upgrade pip && pip install -r ./requirements.txt

