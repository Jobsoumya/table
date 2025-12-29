pipeline {
  agent any

  options {
    timeout(time: 10, unit: 'MINUTES')
  }
  
  environment {
    COMPOSE_FILE = "docker-compose.yml"
  }

  stages {

    stage('Checkout') {
      steps {
        checkout scm
      }
    }

    stage('Quality Checks') {
        parallel {

          stage('Lint') {
              steps {
                  sh 'echo "Run flake8 here"'
              }
          }

          stage('Unit Tests') {
              steps {
                  sh 'echo "Run unit tests here"'
              }
          }
        }  
    }
    stage('Build Images') {
      steps {
        sh 'docker-compose build'
      }
    }

    stage('Start Services') {
      steps {
        sh 'docker-compose up -d --abort-on-container-exit'
      }
    }

    stage('Wait for App Health') {
      steps {
        sh '''
        echo "Waiting for app to become healthy..."
        for i in {1..10}; do
          STATUS=$(docker inspect --format='{{.State.Health.Status}}' python_table || echo "starting")
          if [ "$STATUS" = "healthy" ]; then
            echo "App is healthy"
            exit 0
          fi
          sleep 3
        done
        echo "App failed health check"
        exit 1
        '''
      }
    }

    stage('Smoke Test via Nginx') {
      steps {
        sh 'docker exec nginx_proxy curl -f http://localhost'
      }
    }
  }

  post {
    always {
      sh 'docker-compose down -v || true'
    }
    success {
            echo "Integration tests passed"
    }
    failure {
            echo "Integration tests failed"
    }
  }
}
