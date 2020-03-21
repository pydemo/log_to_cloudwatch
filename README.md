# log_to_cloudwatch
Insert your logs into Amazon CloudWatch using Python

```
#!/usr/local/bin/python3

import boto3
import time


logs = boto3.client('logs', region_name='us-east-1')

LOG_GROUP='TUTORIAL-DEV2'
LOG_STREAM='stream1'

logs.create_log_group(logGroupName=LOG_GROUP)
logs.create_log_stream(logGroupName=LOG_GROUP, logStreamName=LOG_STREAM)


timestamp = int(round(time.time() * 1000))

response = logs.put_log_events(
	logGroupName=LOG_GROUP,
	logStreamName=LOG_STREAM,
	logEvents=[
		{
			'timestamp': timestamp,
			'message': time.strftime('%Y-%m-%d %H:%M:%S')+'\tHello world, here is our first log message!'
		}
	]
)
```
