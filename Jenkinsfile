
def CONTAINER_NAME="flask-app"
def CONTAINER_TAG="latest"
def HTTP_PORT="5000"

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
        imagePrune(CONTAINER_NAME)
        sh "docker build -t $CONTAINER_NAME ."
        
    }
    stage('Deploy'){
        sh "docker run -p $HTTP_PORT:5000 -d $CONTAINER_NAME"
    }
   
}

def imagePrune(containerName){
    try {
        sh "docker image prune -f"
        sh "docker stop $containerName"
    } catch(error){

    }
}