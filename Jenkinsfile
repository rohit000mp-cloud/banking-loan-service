pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                echo 'Checking out GitHub repository'

                git branch: 'main',
                    url: 'https://github.com/rohit000mp-cloud/banking-loan-service.git'
            }
        }

        stage('Build Docker Image') {
            steps {
                echo 'Building loan service Docker image'

                sh 'docker build -t loan-service:v2 .'
            }
        }

        stage('Deploy Loan Service') {
            steps {
                echo 'Deploying loan service'

                sh '''
                    docker rm -f loan-container 2>/dev/null || true

                    docker run -d \
                        --name loan-container \
                        -p 127.0.0.1:5001:5000 \
                        loan-service:v2
                '''
            }
        }

        stage('Health Check') {
            steps {
                echo 'Checking loan application health'

                sh '''
                    for attempt in 1 2 3 4 5 6 7 8 9 10
                    do
                        if curl --fail --silent \
                            --output /dev/null \
                            http://127.0.0.1:5001/loan
                        then
                            echo "Loan application healthy"
                            curl --fail --silent --show-error \
                                http://127.0.0.1:5001/loan
                            exit 0
                        fi

                        echo "Retry attempt $attempt"
                        sleep 3
                    done

                    echo "Health check failed"
                    docker logs --tail 30 loan-container
                    exit 1
                '''
            }
        }
    }

    post {
        success {
            echo 'GitHub webhook CI/CD pipeline successful'
        }

        failure {
            echo 'Pipeline failed. Check console output'
        }
    }
}
