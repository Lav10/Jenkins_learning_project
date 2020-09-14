import boto3

s3_resource = boto3.resource('s3')
bucket = s3_resource.Bucket('test-airflow-bucket')

for bucket_object in bucket.objects.all():
	print(bucket_object)