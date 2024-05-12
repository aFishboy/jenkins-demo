# jenkins-demo

Example repository for ECS 161 Programming Tools Live Demo
```
docker build -t j-image .
```
```
docker run --name j-container --restart=on-failure --detach `
  --network jenkins --env DOCKER_HOST=tcp://docker:2376 `
  --env DOCKER_CERT_PATH=/certs/client --env DOCKER_TLS_VERIFY=1 `
  --volume jenkins-data:/var/jenkins_home `
  --volume jenkins-docker-certs:/certs/client:ro `
  --publish 8080:8080 --publish 50000:50000 j-image
```

## To get the initial admin password use
```
docker exec j-container cat /var/jenkins_home/secrets/initialAdminPassword
```
or
```
docker logs j-container
```

## Next create a freestyle job

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

python3 test_add_two_numbers.py  
python3 helloworld.py

## Pipeline Job

lightweight checkout

## Next go to command line

use 'ngrok http 8080' to open port 8080 to be public
copy  
Forwarding  
https://8071-2600-1700-4421-48b0-2c2e-b2a2-df84-d219.ngrok-free.app

## Go to github webhooks

Enter the ngrok url with /github-webhooks/ appended to the end eg  
https://8071-2600-1700-4421-48b0-2c2e-b2a2-df84-d219.ngrok-free.app/github-webhook/  
add the webhook and check ngrok for POST 200 OK
