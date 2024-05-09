# jenkins-demo

Example repository for ECS 161 Programming Tools Live Demo

docker build -t jenkins demo .

docker run -d -p 8080:8080 -v jenkins_home:/var/jenkins_home --name jenkins-container jenkins-demo

## To get inital admin password use

docker exec jenkins-container cat /var/jenkins_home/secrets/initialAdminPassword

## Next create freestyle job

### Source Code Management  

Git  
url as the http clone with .git at the end  
branch blank  

### Build Triggers

GitHub hook trigger for GITScm polling

### Build Steps

Execute shell

echo "Commit that triggered this job"  
git log -1 HEAD --oneline

## Next go to command line

use 'ngrok http 8080' to open port 8080 to be public
copy  
Forwarding  
https://8071-2600-1700-4421-48b0-2c2e-b2a2-df84-d219.ngrok-free.app

## Go to github webhooks

Enter the ngrok url with /github-webhooks/ appended to the end eg  
https://8071-2600-1700-4421-48b0-2c2e-b2a2-df84-d219.ngrok-free.app/github-webhook/  
add the webhook and check ngrok for POST 200 OK
