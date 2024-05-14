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
