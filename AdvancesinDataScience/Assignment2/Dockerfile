FROM python
RUN pip install requests pandas boto3 botocore boto arrow jupyter notebook seaborn ggplot
COPY ./Assignment2/config.json /
COPY ./Assignment2/dataIngestion.py / 
COPY ./Assignment2/run.sh /
COPY ./Assignment2/logger.log /
COPY ./Assignment2/rawDataEDA.ipynb /
ENTRYPOINT  ["bash", "run.sh"]

