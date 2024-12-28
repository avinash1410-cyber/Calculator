pipeline {
    agent any
    stages {
        stage('Checkout Code') {
            steps {
                git branch: 'backend-dev', url: 'https://github.com/avinash1410-cyber/Calculator.git'
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
        stage('Run Tests') {
            steps {
                sh '''
                    source venv/bin/activate
                    python manage.py test
                '''
            }
        }
    }
}
