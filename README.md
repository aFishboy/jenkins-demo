# jenkins-demo

Example repository for ECS 161 Programming Tools Live Demo

`cd` to the cloned working directory:
```bash
cd jenkins-demo
```
```bash
docker build -t j-image .
```
Windows
```bash
docker run `
  --detach `
  --volume jenkins_home:/var/jenkins_home `
  --publish 9090:8080 `
  --name j-container `
  j-image
```
MacOS / Linux
```bash
docker run \
  --detach \
  --volume jenkins_home:/var/jenkins_home \
  --publish 9090:8080 \
  --name j-container \
  j-image
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
**🚩Note**: It may be fine if you see different output, it may take some time to fully initialize Jenkins.\
Just hang for a bit, and run again.

## Jenkins Web UI
1. Go to `localhost:8080` in any browser (if the port is not conflicted with other software).
2. You should see a prompt for the initial password.
3. Copy and paste the generated password you see in **logs**.
4. In this case, copy and paste *4058081dce434bc88ced0c02ea3f8433*.
5. Then you should be prompted for a series of setups.
6. After the setup, you will see the Jenkins Web UI.

## Freestyle Project
1. Click `Create a job` or `New Item` (left bar)
2. Give a name such as `<demo>`
3. Choose `Freestyle project` below
4. Select `Configure` in the left-hand side menu
5. Refer below for further configuration

### Source Code Management

Select `Git`
- [ ] None
- [x] Git
- Repository URL: `https://github.com/aFishboy/jenkins-demo`
- Branches to build: `main`

### Build Triggers

- [x] GitHub hook trigger for GITScm polling

### Build Steps

in the dropdown menu, select `Execute shell`
Copy and paste the following script in the command textbox:
```
echo "Commit that triggered this job"  
git log -1 HEAD --oneline

python3 test_add_two_numbers.py  
python3 helloworld.py
```

Click `Save`, then you should be redirect back to the `demo`'s `Status` page

### RUNNNN!
On the left-hand side bar, click `Build Now`
You will see a new "build" in the `Build History`
You can click on it and see the output of this build by clicking `Console Output`

## Pipeline Job
1. Click `Create a job` or `New Item` (left bar)
2. Give a name such as `<demo-pipeline>`
3. Choose `Pipeline` below
4. Select `Configure` in the left-hand side menu
5. Refer below for further configuration

### Pipeline Configuration
Scroll all the way down
1. In the `Definition`'s dropdown menu, choose `Pipeline script from SCM`
2. Repository URL: `https://github.com/aFishboy/jenkins-demo`
3. Branches to build: `*/main` or just `main`
4. Uncheck `lightweight checkout`

Click `Save`, then you should be redirect back to the `demo-pipeline`'s `Status` page

### RUNNNN!
On the left-hand side bar, click `Build Now`
You will see a new "build" in the `Build History`
You can click on it and see the output of this build by clicking `Console Output`

## Next go to command line

use 'ngrok http 8080' to open port 8080 to be public
copy  
Forwarding  
https://8071-2600-1700-4421-48b0-2c2e-b2a2-df84-d219.ngrok-free.app

## Go to github webhooks

Enter the ngrok url with /github-webhooks/ appended to the end eg  
https://8071-2600-1700-4421-48b0-2c2e-b2a2-df84-d219.ngrok-free.app/github-webhook/  
add the webhook and check ngrok for POST 200 OK
