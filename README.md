# AWS Lambda functions for Instance Scheduling

Language: **Python**

Using **boto3** library

**Aurora**

Starts or Stops a DB Cluster (AWS does not allow you to stop or start an Aurora instance)

Usage Examples:

Stop a Cluster
```json
{
  "clusters": [
    "my-amazing-aurora-cluster"
  ],
  "action": "stop"
}
```


Credits: 
https://medium.com/cognitoiq/low-hanging-fruit-cutting-your-rds-instance-costs-in-half-736b8b490a24
