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
        stage('Build Docker Image') {
            steps {
                script {
                    // Use correct quotes and interpolate the Dockerfile path
                    docker.build("streamlit-app:latest", "-f ${env.WORKSPACE}/streamlit_reqs .")
                }
            }
        }
        stage('Deploy Docker Container') {
            steps {
                script {
                    // Stop and remove existing containers with the same name
                    sh 'docker stop streamlit-app || true'
                    sh 'docker rm streamlit-app || true'
                    
                    // Run the Docker container
                    docker.image('streamlit-app:latest').run('-p 8501:8501 -d')
                }
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
