# 🗝️ List AWS Secrets

This Python script uses the AWS SDK, Boto3, to list all secrets stored in AWS Secrets Manager.

## 📚 Description

The script connects to AWS Secrets Manager using Boto3 and retrieves a list of all secrets. For each secret, it retrieves the secret value and prints the secret name and value.

## 📦 Installation

1) Clone the repository:

```bash
git clone https://github.com/albertleng/list_aws_secrets.git
```

2) Install the required Python packages:

```bash
pip install -r requirements.txt
```



## 🚀 Usage
1. Ensure you have the necessary AWS credentials configured. You can do this by setting the **AWS_ACCESS_KEY_ID**, **AWS_SECRET_ACCESS_KEY**, and **AWS_SESSION_TOKEN** environment variables, or by using the AWS CLI's **configure** command.
2. Run the script:

```bash
python list_aws_secrets.py
```

## 📖 Sample Usage
```bash
list_aws_secrets on  main [!?] via 🐍 v3.10.0 (.venv) on ☁️  (us-east-1) took 5s 
❯ python list_aws_secrets.py     
Secret Name: MyDatabaseSecret, Secret Value: {"username":"dbuser","password":"dbpassword"}
Secret Name: /prod/username/, Secret Value: {"username":"delfrinando"}
Secret Name: prod/tom, Secret Value: {"production":"tom"}
Secret Name: albert/prod/test/secret, Secret Value: {"OPENAI_API_KEY":"Hahaha"}
Secret Name: prod/mwaiyee, Secret Value: {"secret":"classified"}
Secret Name: prod/nama/, Secret Value: {"nama":"jolchin"}
Secret Name: jeremysecret, Secret Value: {"secretname":"secret20240520"}
Secret Name: prod/tarmizisecret, Secret Value: {"username":"tarmizisulaiman"}
Secret Name: username, Secret Value: {"username":"james"}
Secret Name: prod/dan, Secret Value: {"yjcdaniel":"Dan@AWS2024"}

```