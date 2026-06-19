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
                ssh dhrupal@app-server "
                sleep 10
                curl -f http://localhost:5000
                "
                '''
            }
        }

    }
}
