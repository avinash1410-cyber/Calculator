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
                // Ensure using bash to enable 'source' command
                sh '''
                    python3 -m venv venv
                    bash -c "source venv/bin/activate && pip install -r requirements.txt"
                '''
            }
        }
        stage('Run Tests') {
            steps {
                // Run tests in the activated virtual environment
                sh '''
                    bash -c "source venv/bin/activate && python manage.py test"
                '''
            }
        }
    }
}
