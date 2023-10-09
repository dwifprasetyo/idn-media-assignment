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

        # # Create the Policy Statement
        # policy_statement = iam.PolicyStatement(
        #     actions=["s3:GetObject"],
        #     resources=[f"{my_bucket.bucket_arn}/*"],
        #     effect=iam.Effect.ALLOW,
        #     principals=[iam.ArnPrincipal("*")]  # This allows public access, restrict as needed
        # )

        # # Attach the policy to the bucket using s3.BucketPolicy
        # bucket_policy = s3.BucketPolicy(
        #     self,
        #     "MyBucketPolicy",
        #     bucket=my_bucket,
        #     removal_policy=core.RemovalPolicy.DESTROY  # Use with caution in production
        # )

        # bucket_policy.document.add_statements(policy_statement)

        # Output the S3 bucket name
        output = core.CfnOutput(
            self,
            "MyBucketName",
            value=my_bucket.bucket_name,
            description="Name of the S3 bucket with public access"
        )
