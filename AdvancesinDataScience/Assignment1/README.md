# Instruction to Run the code:

- Download Assignment1 folder from github in to your local machine

- To get the images in the local execute: 
   - docker pull sumedh11/assign1adssummer:latest
   - docker pull sumedh11/assign1part2adssummer:latest
   
## Go in Docker1/FinalDay folder 

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
 
 ## Go in Docker2/Docker2 folder 

-Build the image by using this command by settingthe current directory to the dockerfile location
docker build -t image2 .

-Publishing an image to docker Hub

-Create a docker hub account, create a repository

-Connect to your account
docker login

-Tag your image to be pushed with repository
docker tag image2 sumedh11/assign1part2adssummer:latest

-Push your image o docker hub
docker push sumedh11/assign1part2adssummer:latest

-Pull image
docker pull sumedh11/assign1part2adssummer:latest

# Insights in EDA before cleansing
