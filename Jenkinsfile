pipeline {

    agent any

        environment{
        IMAGE_NAME = "flask-cicd"
        IMAGE_TAG = "${BUILD_NUMBER}"


        DOCKER_HUB_USER = "shivashankar12121"
        DOCKER_CRED_ID = "docker-hub-credentials"

}
    stages {
        stage('Build Docker Image'){

            steps {

                sh "docker build -t ${IMAGE_NAME}:${IMAGE_TAG} ."

                sh "docker tag ${IMAGE_NAME}:${IMAGE_TAG} ${IMAGE_NAME}:latest"

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
                ${IMAGE_NAME}:${IMAGE_TAG}
                '''
            }

        }

      stage('Test Container'){
        steps{
                echo "Hi hello wait for some time"
                sleep 5
                sh "curl --retry 3 --retry-delay 2 --retry-connrefused http://localhost:5000"
}
}

    stage('list Docker images'){
        steps{
                sh 'docker images ls'
}
}

   stage('Push to Dockerhub'){
        steps{
                withCredentials([usernamePassword(credentialsId: "${DOCKER_CRED_ID}", passwordVariable: 'DOCKER_PASSWORD', usernameVariable: 'DOCKER_USERNAME')]) {
                    sh "echo \$DOCKER_PASSWORD | docker login -u \$DOCKER_USERNAME --password-stdin"
                    
                    // Tag image for your specific Docker Hub repository
                    sh "docker tag ${IMAGE_NAME}:${IMAGE_TAG} ${DOCKER_HUB_USER}/${IMAGE_NAME}:${IMAGE_TAG}"
                    sh "docker tag ${IMAGE_NAME}:latest ${DOCKER_HUB_USER}/${IMAGE_NAME}:latest"
                    
                    // Push to registry
                    sh "docker push ${DOCKER_HUB_USER}/${IMAGE_NAME}:${IMAGE_TAG}"
                    sh "docker push ${DOCKER_HUB_USER}/${IMAGE_NAME}:latest"
                }
            }

    }

}

        post {
        // Clean up stage to remove dangling Docker images
        always {
            echo "Cleaning up dangling and unused build images..."
            sh "docker image prune -f"
        }
    }
}
