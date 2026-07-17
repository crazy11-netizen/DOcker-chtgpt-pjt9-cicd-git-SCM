pipeline {

    agent any

    stages {

        stage('Build Docker Image') {

            steps {

                sh 'docker build -t flask-cicd:v1 .'

            }

        }

        stage('Stop Old Container') {

            steps {

                sh 'docker stop flask-app || true'

            }

        }

        stage('Remove Old Container') {

            steps {

                sh 'docker rm flask-app || true'

            }

        }

        stage('Run Container') {

            steps {

                sh '''
                docker run -d \
                --name flask-app \
                -p 5000:5000 \
                flask-cicd:v1
                '''
            }

        }

    }

}
