from aws_cdk import (
    core,
    aws_s3 as s3,
    aws_iam as iam
)

class MyS3BucketStack(core.Stack):

    def __init__(self, scope: core.Construct, id: str, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)

        # Create an S3 bucket with public read access and CORS
        my_bucket = s3.Bucket(
            self,
            'idn-media-assignment-test',
            bucket_name='idn-media-assignment-test',
            versioned=False,  # Set to True if you want versioning
            removal_policy=core.RemovalPolicy.DESTROY,  # Use with caution in production
            block_public_access=s3.BlockPublicAccess(block_public_policy=False),
            cors=[
                s3.CorsRule(
                    allowed_methods=[s3.HttpMethods.GET],
                    allowed_origins=["*"],
                    allowed_headers=["*"]
                )
            ]
        )

        # Grant public read access to all objects in the bucket
        my_bucket.add_to_resource_policy(iam.PolicyStatement(
            actions=["s3:GetObject"],
            resources=[f"{my_bucket.bucket_arn}/*"],
            effect=iam.Effect.ALLOW,
            principals=[iam.ArnPrincipal('*')]
        ))

        # Output the S3 bucket name
        output = core.CfnOutput(
            self,
            "MyBucketName",
            value=my_bucket.bucket_name,
            description="Name of the S3 bucket with public access"
        )
