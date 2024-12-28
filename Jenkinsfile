pipeline {
    agent any
    environment {
        GIT_CREDENTIALS = 'github-https-creds' // Use the ID of your GitHub credentials in Jenkins
    }
    stages {
        stage('Checkout Code') {
            steps {
                // Use HTTPS and the appropriate credentials for authentication
                git branch: 'backend-dev', url: 'https://github.com/avinash1410-cyber/Calculator.git', credentialsId: 'github-https-creds'
            }
        }
        
        stage('Install Dependencies') {
            steps {
                // Use bash explicitly to run the script
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
        
        stage('Push to Main') {
            when {
                branch 'backend-dev' // You can customize this if needed, e.g., only on the 'backend-dev' branch
            }
            steps {
                script {
                    // Only proceed if tests pass
                    if (currentBuild.result == 'SUCCESS') {
                        // Checkout the main branch
                        sh 'git checkout main'
                        
                        // Merge the current branch into the main branch
                        sh 'git merge backend-dev'
                        
                        // Push the changes to the main branch
                        sh 'git push origin main'
                    } else {
                        error "Tests failed. Not merging to main."
                    }
                }
            }
        }
    }
    post {
        success {
            echo 'Tests passed and changes pushed to main branch successfully!'
        }
        failure {
            echo 'Tests failed. Please fix the issues.'
        }
    }
}
