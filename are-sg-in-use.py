import boto3 , sys
ec2 = boto3.resource('ec2')
instance = ec2.instances.all()
sg_id = str(sys.argv)
print sg_id[1:]
for instance in ec2.instances.all():
    #for now only running = 16
    if instance.state['Code'] == 16:
        for i in range(len(instance.security_groups)):
            if instance.security_groups[i]['GroupId'] == sg_id :
                print instance.id
