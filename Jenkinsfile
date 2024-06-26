pipeline{
        agent any
        environment{
            AWS_ACCOUNT_ID='120691575341'
            AWS_DEFAULT_REGION='eu-central-1'
            IMAGE_REPO_NAME='sheikhs'
            IMAGE_TAG='latest'
            REPO_URI="${AWS_ACCOUNT_ID}.dkr.ecr.${AWS_DEFAULT_REGION}.amazonaws.com/${IMAGE_REPO_NAME}"
        }
        stages{
                stage('Tests'){
                        steps{ 
				sh '''
                                python3 -mvenv venv && 
                                . venv/bin/activate && 
                                python -mpip install -r requirements.txt &&
                                coverage run -m pytest tests -v && coverage report -m
                                '''
                        }
                }
                stage('Build Docker Image'){
                        steps{
                                sh "docker build -t ${IMAGE_REPO_NAME}:${IMAGE_TAG} ."
                        }
                }
                stage('Deliver Docker Image to ECR'){
                        steps{
                                script{
                                        sh """
                                        aws ecr get-login-password --region ${AWS_DEFAULT_REGION} | docker login --username AWS --password-stdin ${AWS_ACCOUNT_ID}.dkr.ecr.${AWS_DEFAULT_REGION}.amazonaws.com && 
                                        docker tag ${IMAGE_REPO_NAME}:${IMAGE_TAG} ${REPO_URI}:${IMAGE_TAG} && 
                                        docker push ${AWS_ACCOUNT_ID}.dkr.ecr.${AWS_DEFAULT_REGION}.amazonaws.com/${IMAGE_REPO_NAME}:${IMAGE_TAG}
                                        """
                                }
                        }
                }
        }
}
