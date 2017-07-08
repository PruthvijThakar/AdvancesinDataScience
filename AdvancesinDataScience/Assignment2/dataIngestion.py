
# coding: utf-8

# In[8]:

import boto 
from boto.s3.key import Key
import json
from boto.s3.connection import S3Connection
from boto.s3.key import Key


# In[ ]:

import logging
import time

log_file_name = "logger" + ".log"
logger = logging.getLogger(log_file_name)
hdlr = logging.FileHandler(log_file_name)
formatter = logging.Formatter('%(asctime)s %(levelname)s %(message)s')
hdlr.setFormatter(formatter)
logger.addHandler(hdlr) 


# In[6]:

with open('config.json') as data_file:    
        data1 = json.load(data_file)


# In[9]:

conn = S3Connection(data1['AWSAccess'], data1['AWSSecret'])


# In[12]:

bucket_name = "assignment2info7390"
initial_file = "zillow_clean.csv"
conn.create_bucket(bucket_name)
existingbucket = conn.get_bucket(bucket_name)
initial_data = Key(existingbucket)
initial_data.key = initial_file
   
initial_data.set_contents_from_filename('zillow.csv')


# In[ ]:

logger.info('Successfully uploaded the data to AWS S3 bucket')

