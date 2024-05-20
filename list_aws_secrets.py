import boto3

client = boto3.client('secretsmanager')

response = client.list_secrets()

for secret in response['SecretList']:
    secret_name = secret['Name']
    secret_value_response = client.get_secret_value(SecretId=secret_name)
    if 'SecretString' in secret_value_response:
        secret_value = secret_value_response['SecretString']
    else:
        secret_value = secret_value_response['SecretBinary']
    print(f'Secret Name: {secret_name}, Secret Value: {secret_value}')