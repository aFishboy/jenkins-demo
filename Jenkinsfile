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
            when {
                expression { currentBuild.result == 'SUCCESS' }
            }
            steps {
                echo 'Merging changes into main branch...'
                sh 'git checkout main' // Switch to main branch
                sh 'git merge --no-ff ${env.BRANCH_NAME}' // Merge current branch into main
            }
        }
        stage('Deploy') {
            when {
                expression { currentBuild.result == 'SUCCESS' }
            }
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
