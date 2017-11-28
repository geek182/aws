import boto3
session = boto3.session.Session(profile_name='profile1',region_name='sa-east-1')
#http://boto3.readthedocs.io/en/latest/reference/services/ec2.html#instance
# #list bucket
# s3 = session.resource('s3')

# for bucket in s3.buckets.all():
#     print(bucket.name)

#list ec2
ec2 = session.resource('ec2')

# for instance in ec2.instances.all():
#     print(instance.id, instance.state['Name'])

instances = ec2.instances.filter(Filters=[{'Name': 'tag-value', 'Values': ['INFRA']}])
for instance in instances:
#    print (instance.id, instance.private_ip_address, instance.instance_type, instance.state)
    for tag in instance.tags:
        if 'Name' in tag['Key']:
            name = tag['Value']
            #print name