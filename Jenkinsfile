pipeline {
    agent any
    environment {
        GIT_CREDENTIALS = 'github-https-creds' // Use the ID of your GitHub credentials in Jenkins
        DOCKER_CREDENTIALS = 'dockerhub-credentials' // DockerHub credentials ID from Jenkins
        DOCKER_IMAGE_NAME = '7827303969/calculator-app' // Docker Hub image name, replace with your username
        DOCKER_TAG = 'working' // Tag for the image
    }
    stages {
        stage('Checkout Code') {
            steps {
                // Use HTTPS and the appropriate credentials for authentication
                git branch: 'main', url: 'https://github.com/avinash1410-cyber/Calculator.git', credentialsId: 'github-https-creds'
            }
        }
        
        stage('Install Dependencies') {
            steps {
                // Install dependencies using bash explicitly
                sh '''
                    #!/bin/bash
                    python3 -m venv venv
                    . venv/bin/activate  # Use dot (.) instead of source
                    pip install -r requirements.txt
                '''
            }
        }
        
        stage('Run Tests') {
            steps {
                sh '''
                    #!/bin/bash
                    . venv/bin/activate  # Use dot (.) instead of source
                    python manage.py test
                '''
            }
        }
        
        stage('Build Docker Image') {
            steps {
                script {
                    // Build the Docker image after tests pass
                    sh 'docker build -t $DOCKER_IMAGE_NAME:$DOCKER_TAG .'
                }
            }
        }
        
        stage('Push Docker Image to Docker Hub') {
            steps {
                script {
                    // Log in to Docker Hub using Jenkins credentials and push the image
                    withDockerRegistry(credentialsId: 'dockerhub-credentials') {
                        sh 'docker push $DOCKER_IMAGE_NAME:$DOCKER_TAG'
                    }
                }
            }
        }
    }
    post {
        success {
            echo 'Tests passed, Docker image pushed to Docker Hub successfully!'
        }
        failure {
            echo 'Tests failed. Please fix the issues.'
        }
    }
}
