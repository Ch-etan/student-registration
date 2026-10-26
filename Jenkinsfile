
pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Verify Python') {
            steps {
                sh 'python3 --version'
            }
        }

        stage('Test Student Registration Form') {
            steps {
                sh 'python3 -m unittest -v test_form.py'
            }
        }
    }

    post {
        success {
            echo 'SUCCESS: All registration form tests passed.'
        }
        failure {
            echo 'FAILURE: The pipeline or automated tests failed.'
        }
        always {
            echo 'Pipeline execution completed.'
        }
    }
}
