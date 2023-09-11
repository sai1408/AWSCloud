import boto3
ec2 = boto3.resource('ec2')
for instance in ec2.instances.all():
    print("Instance Id: {0}\nInstance Type: {1}\nInstance AMI: {2}\nInstance State: {3}\n".format(
         instance.id, instance.instance_type, instance.image.id, instance.state
         )
     )
