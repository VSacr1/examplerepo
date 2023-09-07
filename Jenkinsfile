pipeline {
    agent any

    stages {

        stage('TearDown') {
            steps {
              sh'docker-compose down'
              sh'docker-compose down --rmi all'
              }
        }

        stage('build') {
            steps {
              sh'docker-compose up -d'
              }
        }
    }
}
