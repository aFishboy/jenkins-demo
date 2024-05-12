# jenkins-demo

Example repository for ECS 161 Programming Tools Live Demo
```bash
docker build -t j-image .
```
```bash
docker run \
  j-image \
  --name j-container \
  --volume jenkins_home:/var/jenkins_home \
  --volume jenkins-data:/var/jenkins_home \
  --volume jenkins-docker-certs:/certs/client:ro \
  --publish 8080:8080 \
  --publish 50000:50000
  --restart=on-failure \
  --detach \
  --env DOCKER_HOST=tcp://docker:2376 \
  --env DOCKER_CERT_PATH=/certs/client \
  --env DOCKER_TLS_VERIFY=1 \
```

## To get the initial admin password use
```bash
docker exec j-container cat /var/jenkins_home/secrets/initialAdminPassword
```
or
```bash
docker logs j-container
```
look for the logs for lines of stars:
```bash output
...
2024-05-12 19:48:16.576+0000 [id=33]    INFO    jenkins.install.SetupWizard#init:

*************************************************************
*************************************************************
*************************************************************

Jenkins initial setup is required. An admin user has been created and a password generated.
Please use the following password to proceed to installation:

4058081dce434bc88ced0c02ea3f8433

This may also be found at: /var/jenkins_home/secrets/initialAdminPassword

*************************************************************
*************************************************************
*************************************************************

2024-05-12 19:48:20.573+0000 [id=33]    INFO    jenkins.InitReactorRunner$1#onAttained: Completed initialization
...
```

## Jenkins Web UI
1. Go to `localhost:8080` in any browser (if the port is not conflicted with other software).
2. You should see a prompt for the initial password.
3. Copy and paste the generated password you see in **logs**.
4. In this case, copy and paste *4058081dce434bc88ced0c02ea3f8433*.
5. Then you should be prompted for a series of setups.
6. After the setup, you will see the Jenkins Web UI.

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
