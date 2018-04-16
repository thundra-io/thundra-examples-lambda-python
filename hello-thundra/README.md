# Hello Thundra Example


This is a simple example to trace your lambda go functions with [Thundra](https://www.thundra.io/).


## How to run using serverless

1 - From thundra-examples-lambda-python/hello-thundra directory, run:

```bash
pip3 install thundra -t .
```

2 - **Login** to [Thundra](https://www.thundra.io/) to create your API key:

![create-api-key](../readme-src/create-api-key.gif)

3 - Paste your API key to serverless.yml and also set your AWS S3 deployment bucket:

```
custom:
    deploymentBucket: <your-s3-deployment-bucket>
    thundraApiKey: <your-api-key>
    ...
```

4 - From thundra-examples-lambda-python/hello-thundra directory, run:

```bash
sls deploy
```

6 - From thundra-examples-lambda-python/hello-thundra directory, run:

```bash
sls invoke --function hello-thundra --data '{"message":"Hello Thundra!"}'
```

5 - Visit [Thundra](https://www.thundra.io/) to observe your metrics. It might take 1-2 minutes to be visible.




