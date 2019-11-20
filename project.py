import boto3
import click

session = boto3.Session(profile_name='Jandro')
ec2 = session.resource('ec2',region_name='eu-west-1')

@click.command()
def list_instances():
    "List EC2 instances"
    for i in ec2.instances.all():
        print(i.id, i.instance_type, i.state['Name'])


if __name__ == "__main__":
    list_instances()