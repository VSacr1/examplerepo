pipeline {
    agent any

    stages {
        stage('Install') {
            steps {
              sh 'ls'
              sh 'python3 -m pip install --upgrade pip'
              sh 'python3 -m pip install flask'
              sh 'python3 -m pip install flask-sqlalchemy'
            }
        }
        stage('build') {
            steps {
              sh'python3 create.py'
              sh 'python3 app.py'
              }
        }
    }
}
