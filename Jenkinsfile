pipeline {
    agent any
    
    stages {
        stage('Build') {
            steps {
                echo 'Installing dependencies...'
                sh 'pip install -r requirements.txt'
            }
        }
        stage('Test') {
            steps {
                echo 'Running tests...'
                sh 'python3 test_homepage.py'
            }
        }
        stage('Deploy') {
            steps {
                echo 'Deploying to production environment...'
                sh 'streamlit run homepage.py'
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
