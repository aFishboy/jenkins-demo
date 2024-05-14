pipeline {
    agent any
    
    stages {
        stage('Build') {
            steps {
                echo "If a build is needed"
            }
        }
        stage('Install Streamlit') {
            steps {
                script {
                    // Update package lists and install Python and python3-venv
                    sh 'apt update'
                    sh 'apt install -y python3 python3-venv'
                    
                    // Create a virtual environment
                    sh 'python3 -m venv venv'
                    
                    // Activate the virtual environment and install Streamlit
                    sh '. venv/bin/activate && pip install streamlit'
                }
            }
        }
        stage('Test') {
            steps {
                script {
                    // Activate the virtual environment before running tests
                    sh '. venv/bin/activate && python3 test_homepage.py'
                }
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
