from aws_cdk import (
    core,
    aws_s3 as s3,
    aws_iam as iam
)

class MyS3BucketStack(core.Stack):

    def __init__(self, scope: core.Construct, id: str, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)

        # Create an S3 bucket with public access
        my_bucket = s3.Bucket(
            self,
            'idn-media-assignment-test',
            versioned=False,  # Set to True if you want versioning
            removal_policy=core.RemovalPolicy.DESTROY  # Use with caution in production
        )

        # Enable public read access for objects in the bucket
        my_bucket.add_to_resource_policy(
            statement=iam.PolicyStatement(
                actions=["s3:GetObject"],
                resources=[f"{my_bucket.bucket_arn}/*"],
                effect=iam.Effect.ALLOW,
                principals=[iam.ArnPrincipal("*")]  # This allows public access, restrict as needed
            )
        )

        # Output the S3 bucket name
        output = core.CfnOutput(
            self,
            "MyBucketName",
            value=my_bucket.bucket_name,
            description="Name of the S3 bucket with public access"
        )
