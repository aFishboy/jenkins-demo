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
                script {
                    echo 'Merging changes into main branch...'
                    println GIT_BRANCH
                    def branchName = GIT_BRANCH.tokenize('/').last()
                    println branchName
                    withCredentials([usernamePassword(credentialsId: 'github_creds', passwordVariable: 'GIT_PASSWORD', usernameVariable: 'GIT_EMAIL')]) {
                        sh "git config --global user.email ${GIT_EMAIL}"
                        sh 'git config --global user.name aFishboy'
                        sh 'git checkout main'
                        sh "git merge --no-ff ${GIT_BRANCH}"
                        sh 'git push'
                    }
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
