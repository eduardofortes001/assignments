import boto3

def lambda_handler(event, context):
    
    session=boto3.session.Session()
    client=session.client(service_name="ec2",region_name="us-east-1")
    list_a = []
    sum_ts = 0
    
    if event["Instance"] == "*":
        response = client.describe_instances()
        for reservation in response['Reservations']:
            for instance in reservation['Instances']:
                volumes = client.describe_volumes(Filters=[{'Name':'attachment.instance-id','Values':[instance['InstanceId']],}])
                if 'PublicIpAddress' in instance.keys():
                        sum_ds = 0
                        for disk in volumes['Volumes']:
                            sum_ds = sum_ds + disk['Size']
                        list_a.append([instance['InstanceId'], instance['InstanceType'], instance['State']['Name'], instance['PrivateIpAddress'], instance['PublicIpAddress'], sum_ds])  
                        sum_ts = sum_ts + sum_ds
                else:
                    sum_ds = 0
                    for disk in volumes['Volumes']:
                        sum_ds = sum_ds + disk['Size']
                    list_a.append([instance['InstanceId'], instance['InstanceType'], instance['State']['Name'], instance['PrivateIpAddress'],'' , sum_ds]) 
                    sum_ts = sum_ts + sum_ds
    else:
        
        try:
            response = client.describe_instances(Filters=[],InstanceIds=[event['Instance'],])
            for reservation in response['Reservations']:
                for instance in reservation['Instances']:
                    volumes = client.describe_volumes(Filters=[{'Name':'attachment.instance-id','Values':[instance['InstanceId']],}])
                    if 'PublicIpAddress' in instance.keys():
                            sum_ds = 0
                            for disk in volumes['Volumes']:
                                sum_ds = sum_ds + disk['Size']
                            list_a.append([instance['InstanceId'], instance['InstanceType'], instance['State']['Name'], instance['PrivateIpAddress'], instance['PublicIpAddress'], sum_ds])  
                            sum_ts = sum_ts + sum_ds
                    else:
                        sum_ds = 0
                        for disk in volumes['Volumes']:
                            sum_ds = sum_ds + disk['Size']
                        list_a.append([instance['InstanceId'], instance['InstanceType'], instance['State']['Name'], instance['PrivateIpAddress'],'' , sum_ds]) 
                        sum_ts = sum_ts + sum_ds
        except:
            m = [ "Invalid or Inexistent Instance Id" ]
            return m
                
    final_list = sorted(list_a, key=lambda k: k[5], reverse=True)
    
    final_list.append(sum_ts)
    
    return final_list

    
