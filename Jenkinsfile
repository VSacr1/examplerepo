pipeline {
    agent any

    stages {
        stage('Install') {
            steps {
              sh 'ls'
              sh'python3 -m pip install requirement.txt'  
            }
        }
        stage('build') {
            steps {
              sh'python3 create.py'
              sh 'python3 app.py3'
              }
        }
    }
}
