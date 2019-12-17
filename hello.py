import boto3
import textwrap


class WellnessModoki:

    # wellness-modokiの初期値設定
    def __init__(self, bucket_name, file_name):
        self.bucket = bucket_name
        self.file = file_name

    def show_weight(self):
        # boto3でs3を使用できるようにする
        # aws configureコマンドを使用してでaccess_key・secret_key・region設定済み
        s3 = boto3.resource('s3')

        # 全バケットを取得して、1つずつprint文で出力する
        # for bucket in s3.buckets.all():
        #     print(bucket.name)

        # オブジェクト取得設定
        obj = s3.Object(self.bucket, self.file)

        # print(obj.key)

        # オブジェクトを取得
        response = obj.get()
        # 取得したオブジェクトの中身を取得
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


bucket = 'dabo3-sample'
file = 'test.txt'
wellness = WellnessModoki(bucket, file)
wellness.show_weight()
