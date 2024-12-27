pipeline {
    agent any
    environment {
        DOCKER_HUB_USERNAME = credentials('7827303969')
        DOCKER_HUB_PASSWORD = credentials('Kumar@2501')
    }
    stages {
        stage('Checkout Code') {
            steps {
                git branch: 'main', url: 'https://github.com/avinash1410-cyber/Calculator.git'
            }
        }
        stage('Install Dependencies') {
            steps {
                sh '''
                    python3 -m venv venv
                    source venv/bin/activate
                    pip install -r requirements.txt
                '''
            }
        }
        // Remove or comment out the test stage
        // stage('Run Tests') {
        //     steps {
        //         sh '''
        //             source venv/bin/activate
        //             python manage.py test
        //         '''
        //     }
        // }
        stage('Build Docker Image') {
            steps {
                sh 'docker build -t ${DOCKER_HUB_USERNAME}/my-calc-backend:latest .'
            }
        }
        stage('Push Docker Image') {
            steps {
                sh '''
                    echo $DOCKER_HUB_PASSWORD | docker login -u $DOCKER_HUB_USERNAME --password-stdin
                    docker push ${DOCKER_HUB_USERNAME}/my-calc-backend:latest
                '''
            }
        }
    }
}
