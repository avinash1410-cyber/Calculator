pipeline {
    agent any
    environment {
        GIT_CREDENTIALS = 'github-https-creds'
        DOCKER_CREDENTIALS = 'dockerhub-credentials'
        DOCKER_IMAGE_NAME = '7827303969/calculator-app'
        DOCKER_TAG = "build-${env.BUILD_NUMBER}"
    }
    stages {
        stage('Checkout Code') {
            steps {
                git branch: 'main', url: 'https://github.com/avinash1410-cyber/Calculator.git', credentialsId: 'github-https-creds'
            }
        }
        stage('Install Dependencies') {
            steps {
                sh '''
                    #!/bin/bash
                    apt-get update && apt-get install -y python3-venv
                    python3 -m venv venv
                    . venv/bin/activate
                    pip install -r requirements.txt
                '''
            }
        }
        stage('Run Tests') {
            steps {
                sh '''
                    #!/bin/bash
                    . venv/bin/activate
                    python manage.py test
                '''
            }
        }
        stage('Build Docker Image') {
            steps {
                echo 'IN DOCKER BUILD'
                sh 'docker build -t $DOCKER_IMAGE_NAME:$DOCKER_TAG .'
                echo 'DOCKER BUILD ENDED'
            }
        }
        stage('Push Docker Image') {
            steps {
                withDockerRegistry(credentialsId: 'dockerhub-credentials') {
                    echo 'IN DOCKER PUSH'
                    sh 'docker push $DOCKER_IMAGE_NAME:$DOCKER_TAG'
                    echo 'DOCKER PUSH ENDED'
                }
            }
        }
    }
    post {
        success {
            echo 'Pipeline executed successfully!'
        }
        failure {
            echo 'Pipeline failed. Check logs for details.'
        }
    }
}
