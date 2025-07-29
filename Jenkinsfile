pipeline {
    agent any
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
                echo 'Deploying your FastAPI app (optional)'
            }
        }
    }
}
