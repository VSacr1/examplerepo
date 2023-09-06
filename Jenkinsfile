pipeline {
    agent any

    stages {

        stage('build') {
            steps {
              sh'docker build -t flask-app .'
              sh'docker run -d --network my-network -p 5000:5000 --name flask-app flask-app'
              }
        }
    }
}
