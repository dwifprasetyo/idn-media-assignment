#!/usr/bin/python3

from aws_cdk import core
from s3_bucket_stack.s3_bucket_stack import MyS3BucketStack

app = core.App()
MyS3BucketStack(app, "MyS3BucketStack")
app.synth()
