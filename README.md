# RandomGov

A Twitter bot that periodically spits out a random page from [gov.uk](gov.uk).

Check it out [here](www.twitter.com/randomgov)

## Deployment

Deployment is very ugly at the minute. Look at improving this!

Make sure the following packages are locally installed to `package/`:
- boto3
- bs4
- tweepy

...by doing `pip3 install --target ./package <PACKAGE>`

```
rm function.zip
cd package/
zip -r9 ${OLDPWD}/function.zip .
cd ..
zip -g function.zip randomgov.py
aws lambda update-function-code --function-name random-gov --zip-file fileb://function.zip
```

## How did I do any of this?

Let's be honest, you'll have forgotten all of this in the morning.

The bot is made up of a Python lambda deployed to AWS. It reads our Twitter secrets out of
AWS Secrets Manager. It's periodically triggered by a Cloudwatch Rule.

### Resources followed

- https://docs.aws.amazon.com/lambda/latest/dg/python-programming-model.html
- https://docs.aws.amazon.com/lambda/latest/dg/lambda-python-how-to-create-deployment-package.html
- https://aws.amazon.com/blogs/aws/aws-secrets-manager-store-distribute-and-rotate-credentials-securely/
- https://docs.aws.amazon.com/AmazonCloudWatch/latest/events/RunLambdaSchedule.html