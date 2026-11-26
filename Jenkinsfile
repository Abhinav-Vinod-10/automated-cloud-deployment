
pipeline {
    agent any

    stages {
        stage('Install Dependencies') {
            steps {
                sh '''
                    python3 -m venv .venv
                    .venv/bin/python -m pip install -r requirements.txt
                '''
            }
        }

        stage('Run Tests') {
            steps {
                sh '.venv/bin/python -m pytest -v'
            }
        }

        stage('Build Docker Image') {
            steps {
                sh 'docker build -t cloud-deployment-app:${BUILD_NUMBER} .'
            }
        }

        // NEW STAGE STARTS HERE

        stage('Push to Docker Hub') {
            steps {
                withCredentials([usernamePassword(
                    credentialsId: 'dockerhub-credentials',
                    usernameVariable: 'DOCKER_USER',
                    passwordVariable: 'DOCKER_TOKEN'
                )]) {
                    sh '''
                        set +x
                        trap 'docker logout' EXIT

                        printf '%s' "$DOCKER_TOKEN" | docker login -u "$DOCKER_USER" --password-stdin

                        docker tag cloud-deployment-app:${BUILD_NUMBER} $DOCKER_USER/cloud-deployment-app:${BUILD_NUMBER}

                        docker push $DOCKER_USER/cloud-deployment-app:${BUILD_NUMBER}
                    '''
                }
            }
        }

        // NEW STAGE ENDS HERE
    }

    post {
        success {
            echo 'Pipeline completed successfully!'
        }
        failure {
            echo 'Pipeline failed!'
        }
    }
}
