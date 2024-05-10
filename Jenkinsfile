pipeline {
    agent any
    
    options {
        // Specify Git checkout options
        scm {
            git {
                // Configure Git repository URL
                remote {
                    url 'your_git_repository_url_here'
                }
                // Fetch changes from all branches
                refspec '+refs/heads/*:refs/remotes/origin/*'
            }
        }
    }
    
    stages {
        stage('Build') {
            steps {
                // Your build steps here
                echo 'Building...'
                sh 'python3 helloworld.py'
            }
        }
        stage('Test') {
            steps {
                // Your test steps here
                echo 'Testing...'
                sh 'python3 test_add_two_numbers.py'
            }
        }
        stage('Deploy to Staging') {
            steps {
                // Your deployment steps here
                echo 'Deploying to staging environment...'
            }
        }
        stage('Deploy to Production') {
            steps {
                // Your deployment steps here
                echo 'Deploying to production environment...'
            }
        }
    }
    
    post {
        success {
            // Actions to take on successful completion of pipeline
            echo 'Pipeline succeeded!'
        }
        failure {
            // Actions to take on failure of pipeline
            echo 'Pipeline failed!'
        }
        always {
            // Actions to take regardless of pipeline result
            echo 'Pipeline finished!'
        }
    }
}

