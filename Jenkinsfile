pipeline {
    agent any

    stages {

        stage('Run Selenium Tests with pytest') {
            steps {
                echo "Running Selenium Tests using pytest"

                // Install dependencies
                bat 'pip install -r requirements.txt'

                // Start Flask app in background (Windows syntax)
                bat 'start /B python app.py'

                // Wait for Flask to start (approx. 5 seconds)
                bat 'ping 127.0.0.1 -n 5 > nul'

                // Run Selenium tests
                bat 'pytest -v'
            }
        }

        stage('Build Docker Image') {
            steps {
                echo "Building Docker Image"
                bat 'docker build -t formvalidation:v8 .'
            }
        }

        stage('Docker Login') {
            steps {
                echo "Logging into Docker Hub"
                // Replace with your actual Docker Hub username/password or Jenkins credentials ID
                bat 'docker login -u rohinigarlapati -p Potatotabla1.'
            }
        }

        stage('Push Docker Image to Docker Hub') {
            steps {
                echo "Pushing Docker Image to Docker Hub"
                bat 'docker tag formvalidation:v1 rohinigarlapati/sample:formvalidationimage:v8'
                bat 'docker push rohinigarlapati/sample:formvalidationimage:v8'
            }
        }

        stage('Deploy to Kubernetes') {
            steps {
                echo "Deploying to Kubernetes Cluster"
                bat 'kubectl apply -f deployment.yaml --validate=false'
                bat 'kubectl apply -f service.yaml'
            }
        }
    }

    post {
        success {
            echo 'Pipeline completed successfully!'
        }
        failure {
            echo 'Pipeline failed. Please check the logs.'
        }
    }
}
