pipeline {
    agent none 
    stages {
        stage('Build') { 
            agent {
                docker {
                    image 'python:3' 
                }
            }
            steps {
                sh 'pip install -r requirements.txt' 
                // sh 'python test.py' 
                sh 'python exec_test.py'
            }

        }
    }
  
}