pipeline {
agent any

stages {

    stage('Deploy Flask App') {
        steps {
            sh '''
            ssh dhrupal@app-server "
            cd ~/flask-mysql-app &&
            git pull &&
            docker compose up -d --build
            "
            '''
        }
    }

    stage('Health Check') {
        steps {
            sh '''
            curl -f http://192.168.109.52:5000
            '''
        }
    }

}

}

