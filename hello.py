import boto3
import textwrap

s3 = boto3.resource('s3')

# for bucket in s3.buckets.all():
#     print(bucket.name)

bucket = 'dabo3-sample'
file = 'test.txt'

obj = s3.Object(bucket, file)

# print(obj.key)

response = obj.get()
body = response['Body'].read()

# print(type(body))

message = body.decode('utf-8')

message_list = message.splitlines()
message_list.append('112.4')

for xx in message_list:
    text = f'''

    あなたの本日の体重は
    
    {xx}kg
    
    '''
    print(repr(text))
    print('-----------')
    print(repr(textwrap.dedent(text)))

