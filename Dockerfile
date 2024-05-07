FROM jenkins/jenkins

USER jenkins

RUN jenkins-plugin-cli --plugins docker-workflow:572.v950f58993843 \
    && jenkins-plugin-cli --plugins atlassian-bitbucket-server-integration:4.0.0