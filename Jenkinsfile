pipeline {
    agent any
    
    stages {
        stage('Build') {
            steps {
                echo 'Building...'
                sh 'python3 helloworld.py'
            }
        }
        stage('Test') {
            steps {
                echo 'Testing...'
                sh 'python3 test_add_two_numbers.py'
            }
        }
        stage('Merge Changes') {
            steps {
                echo 'Merging changes into main branch...'
                println GIT_BRANCH
                withCredentials([usernamePassword(credentialsId: 'your_git_credentials_id', passwordVariable: 'GIT_PASSWORD', usernameVariable: 'GIT_USERNAME')]) {
                    sh "git config --global user.email ${GIT_EMAIL}"
                    sh 'git checkout main'
                    sh "git merge --no-ff ${GIT_BRANCH}"
                }
            }
        }
        stage('Deploy') {
            steps {
                echo 'Deploying to production environment...'
                // Your deployment steps here
            }
        }
    }
    
    post {
        success {
            echo 'Pipeline succeeded!'
        }
        failure {
            echo 'Pipeline failed!'
        }
        always {
            echo 'Pipeline finished!'
        }
    }
}
