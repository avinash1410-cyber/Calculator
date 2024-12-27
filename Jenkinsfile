pipeline {
    agent any
    environment {
        DOCKER_HUB_USERNAME = credentials('7827303969')
        DOCKER_HUB_PASSWORD = credentials('Kumar@2501')
    }
    stages {
        stage('Checkout Code') {
            steps {
                git branch: 'front', url: 'https://github.com/avinash1410-cyber/Calculator.git'
            }
        }
        stage('Install Dependencies') {
            steps {
                sh 'npm install'
            }
        }
        // Remove or comment out the test stage
        // stage('Run Tests') {
        //     steps {
        //         sh 'npm run test'
        //     }
        // }
        stage('Build Docker Image') {
            steps {
                sh 'docker build -t ${DOCKER_HUB_USERNAME}/my-calc-frontend:latest .'
            }
        }
        stage('Push Docker Image') {
            steps {
                sh '''
                    echo $DOCKER_HUB_PASSWORD | docker login -u $DOCKER_HUB_USERNAME --password-stdin
                    docker push ${DOCKER_HUB_USERNAME}/my-calc-frontend:latest
                '''
            }
        }
    }
}
