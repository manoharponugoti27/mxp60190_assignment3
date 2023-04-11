import boto3

# Initialize the SNS client
sns_client = boto3.client('sns')

# Create an SNS topic
topic_name = 'my-topic'
response = sns_client.create_topic(Name=topic_name)
topic_arn = response['TopicArn']

# Add an email subscription to the topic
email_address = 'mxp60190@ucmo.edu'
sns_client.subscribe(
    TopicArn=topic_arn,
    Protocol='email',
    Endpoint=email_address
)

# Print the ARN of the topic
print(f"Topic ARN: {topic_arn}")