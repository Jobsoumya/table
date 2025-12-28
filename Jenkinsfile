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

    stage('Build Images') {
      steps {
        sh 'docker-compose build'
      }
    }

    stage('Start Services') {
      steps {
        sh 'docker-compose up -d'
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
        sh 'curl -f http://localhost:8081'
      }
    }
  }

  post {
    always {
      sh 'docker-compose down -v'
    }
  }
}
