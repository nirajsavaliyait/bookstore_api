pipeline {
    agent {
        docker {
            image 'python:3.11'
        }
    }
    stages {
        stage('Install dependencies') {
            steps {
                sh 'pip install -r requirements.txt'
            }
        }
        stage('Run Tests') {
            steps {
                sh 'pytest'
            }
        }
        stage('Deploy') {
            steps {
                echo 'Deploying the application...'
                // Add deploy logic here
            }
        }
    }
}
