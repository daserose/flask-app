pipeline {
    agent { docker { image 'test:flask-2' } }

    stages {
        stage('1-Build') {
            steps {
                echo "Start of Stage Build"
                echo "Building......."
                sh   "python --version"
                echo "End of Stage Build"
            }
        }
        stage('2-Test') {
            steps {
                echo "Start of Stage Test"
                echo "Testing......."
                echo "End of Stage Build"
            }
        }
        stage('3-Deploy') {
            steps {
                echo "Start of Stage Deploy"
                echo "Deploying......."
                echo "End of Stage Build"
            }
        }
   }
}
