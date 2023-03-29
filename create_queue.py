import boto3

# Create an SQS client
sqs = boto3.client('sqs')

# Set the queue name
queue_name = 'mysection'

# Create a new SQS queue
response = sqs.create_queue(QueueName=queue_name)

# Print the URL of the new queue
print(response['QueueUrl'])
