The aim is to create a REST API using the zillow dataset and Creating Data as a Service application.

Link to dataset: https://www.kaggle.com/c/zillow-prize-1/data


# Instruction to Run the code:

- Download Assignment2 folder from github in to your local machine

- To get the images in the local execute: 
   - docker pull sumedh11/assignment2team4
   
## Go in Assignment2 folder 

-docker build -t image1 .

-Publishing an image to docker Hub

-Create a docker hub account, create a repository

-Connect to your account
docker login

-Tag your image to be pushed with repository
docker tag image1 sumedh11/assign1adssummer:latest

-Push your image o docker hub
docker push sumedh11/assign1adssummer:latest

-Pull image
docker pull sumedh11/assign1adssummer:latest
 - The commit is necessary after each time the image is run so that the data doesnt get lost.
 
# The rawDataEDA file shows the insights we can infer from the Zillow dataset that we are given and link is mentioned at the start of README.

# The file REST_API.ipynb shows the script for uploading the data to Google Bigquery platform and how to create an API to access the same.

-It also contains the method for pulling out 10 nearest locations based on the longitude and latitude entered by the user and the method is integrated to the Google Bigquery platform.

-This file contains a POST and a GET method which enhances the api we created by posting the data on cloud and getting the 10 nearest locations based on real inputs by users.



