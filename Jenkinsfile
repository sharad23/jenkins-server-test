def IMAGE_NAME="flask-app"
def CONTAINER_NAME ="wolawitz"
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
        sh "docker build -t $IMAGE_NAME ."
        
    }
    stage('Deploy'){
        sh "docker run -p $HTTP_PORT:5000 -d --name=$CONTAINER_NAME  $IMAGE_NAME"
    }
   
}

def imagePrune(containerName){
    try {
        sh "docker image prune -f"
        sh "docker stop $containerName"
        sh "docker rm $containerName"
    } catch(error){
        sh "echo $error"
    }
}