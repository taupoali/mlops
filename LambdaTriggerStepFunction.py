import boto3,logging
import json
logger = logging.getLogger()
logger.setLevel(logging.INFO)

stepFunction = boto3.client('stepfunctions')

def lambda_handler(event, context):
  try:
    logger.info(event)
  
    response = stepFunction.start_execution(
      stateMachineArn='arn:aws:states:us-east-1:779527000053:stateMachine:TrainingStateMachine-fL4fPKOcTkI4',
      input = json.dumps(event, indent=4))
  except Exception as e:
      print(f'Error: {str(e)}')
