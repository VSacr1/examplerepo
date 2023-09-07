pipeline {
    agent any

    stages {

        stage('build') {
            steps {
              sh'docker-compose down'
              sh'docker-compose up -d'
              }
        }
    }
}
