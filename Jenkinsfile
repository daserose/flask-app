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
        stage('deployment') {
            steps {
                kubernetesDeploy (
                    kubeconfigId: 'kubeconfig',
                    configs: 'kube.yml',
                    enableConfigSubstitution: true
                )
            }
        }
    }
}
