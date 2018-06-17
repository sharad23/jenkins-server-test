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
        }
        
      
    }
  
}
node {
    stage('Build') {
        sh 'docker build -t flask-app .' 
        
    }
    stage('Deploy'){
        sh 'docker run -p 5000:5000 -d flask-app'
    }
    stage('Extra'){
        sh 'docker-compose '
    }
}