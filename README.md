# RandomGov

A Twitter bot that periodically spits out a random page from [gov.uk](gov.uk).

Check it out [here](www.twitter.com/randomgov)

## Setup

Create a Twitter bot, and copy API keys in to AWS Secrets Manager. Inside of a secret named
`RandomGovTwitter`, ensure you have:
- `RandomGovConsumerKey`
- `RandomGovConsumerSecret`
- `RandomGovAccessToken`
- `RandomGovAccessTokenSecret`

Deployment is managed by the [Serverless Framework](https://serverless.com/).

To deploy, make sure you are authenticated against AWS and then run:

```
serverless deploy
```

To deploy production, append `--stage prod`.

Once deployed, set up a CloudWatch Rule to periodically trigger the lambda.

## How did I do any of this?

Let's be honest, you'll have forgotten all of this in the morning.

The bot is made up of a Python lambda deployed to AWS. It reads our Twitter secrets out of
AWS Secrets Manager. It's periodically triggered by a Cloudwatch Rule.

## Dependencies

- Node
- Serverless Framework
- Python 3.7

(Python packages, as specified by `requirements.txt`)
- boto3
- bs4
- tweepy

### Resources followed

- https://docs.aws.amazon.com/lambda/latest/dg/python-programming-model.html
- https://docs.aws.amazon.com/lambda/latest/dg/lambda-python-how-to-create-deployment-package.html
- https://aws.amazon.com/blogs/aws/aws-secrets-manager-store-distribute-and-rotate-credentials-securely/
- https://docs.aws.amazon.com/AmazonCloudWatch/latest/events/RunLambdaSchedule.html
- https://serverless.com/blog/serverless-python-packaging/