node {
    
    stage('exec'){
        agent {
                docker {
                    image 'python:3' 
                }
        }
        sh "python test.py"
    }

}