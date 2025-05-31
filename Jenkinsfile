pipeline {
    agent any
    environment {
        IMAGE_NAME = "flask-ci-demo"
        CONTAINER_NAME = "flask_app"
    }

    stages {
        stage('Checkout') {
            steps {
                git branch: 'main', url: 'https://github.com/Kelebek16/flask-ci-demo.git'
            }
        }

        stage('Build Docker Image') {
            steps {
                sh 'docker build -t $IMAGE_NAME .'
            }
        }

        stage('Run Container') {
            steps {
                script {
                    sh 'docker rm -f $CONTAINER_NAME || true'
                    sh 'docker run -d --name $CONTAINER_NAME -p 5000:5000 $IMAGE_NAME'
                }
            }
        }
    }

    post {
        failure {
            echo "🚨 Build başarısız oldu, rollback başlatılabilir."
        }
    }
}
