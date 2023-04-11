import boto3

# create SNS client
sns = boto3.client('sns')

# create SNS topic
response = sns.create_topic(Name='my-topic')

# get topic ARN
topic_arn = response['TopicArn']

# add email as subscriber
sns.subscribe(
    TopicArn=topic_arn,
    Protocol='email',
    Endpoint='mxp60190@edu.com'
)
