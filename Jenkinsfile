pipeline {
    agent any
    stages {
        stage('docker-compose build') {
            steps {
                sh 'cat docker-compose.yml'
                sh 'docker-compose build'
            }
        }
        stage('docker-compose up') {
            steps {                
                sh 'docker-compose up -d'
            }
        }
    }
}
