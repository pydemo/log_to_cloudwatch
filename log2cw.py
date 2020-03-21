#!/usr/local/bin/python3

import boto3
import time

LOG_GROUP='TUTORIAL-DEV2'
LOG_STREAM='stream1'


	
def create_log(client):





	client.create_log_group(logGroupName=LOG_GROUP)
	client.create_log_stream(logGroupName=LOG_GROUP, logStreamName=LOG_STREAM)


	timestamp = int(round(time.time() * 1000))

	response = client.put_log_events(
		logGroupName=LOG_GROUP,
		logStreamName=LOG_STREAM,
		logEvents=[
			{
				'timestamp': timestamp,
				'message': time.strftime('%Y-%m-%d %H:%M:%S')+'\tHello world, here is our first log message!'
			}
		]
	)


def get_log_events(client, log_group):
	"""List the first 10000 log events from a CloudWatch group.

	:param log_group: Name of the CloudWatch log group.

	"""

	resp = client.filter_log_events(logGroupName=log_group, limit=10000)
	return resp['events']


if __name__ == '__main__':
	client = boto3.client('logs', region_name='us-east-1')
	for event in get_log_events(client, LOG_GROUP):
		print(event)
		
		
