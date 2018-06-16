pipeline {
    agent none 
    stages {
        stage('Test') { 
            agent {
                docker {
                    image 'python:3' 
                }
            }
            steps {
                sh 'pip install -r requirements.txt' 
                sh 'python exec_test.py'
            }
            post {
                always {
                    sh 'echo "I will always be with u rishu"'
                }
                failure {
                    sh 'echo "There is a failure"'
                }
                success {
                    sh 'echo "There is a success"'
                }

            }

        }
        stage('Build') {
            agent {
                docker {
                    image 'python:3'
                }
            }
            steps {
                sh 'python test.py' 
            }
        }
       
    }
  
}