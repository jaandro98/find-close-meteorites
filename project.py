import boto3

session = boto3.Session(profile_name='Jandro')
ec2 = session.resource('ec2',region_name='eu-west-1')

for i in ec2.instances.all():
    print(i)