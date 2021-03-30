from aws_cdk import (
    core as cdk,
    aws_s3 as _s3
)

# For consistency with other languages, `cdk` is the preferred import name for
# the CDK's core module.  The following line also imports it as `core` for use
# with examples from the CDK Developer's Guide, which are in the process of
# being updated to use `cdk`.  You may delete this import if you don't need it.
from aws_cdk import core
from pyboto3 import *
import boto3


class CdkLearnStack(cdk.Stack):

    def __init__(self, scope: cdk.Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # The code that defines your stack goes here
        
        _s3.Bucket(
            self,
            "mybucketid",
            bucket_name = "prasadrenmuka3010",
            versioned=True,
            encryption=_s3.BucketEncryption.S3_MANAGED,
            block_public_access=_s3.BlockPublicAccess.BLOCK_ALL

        )

        mybuck = _s3.Bucket(
            self,
            "myBuckId",
            bucket_name="renukadeepu3003"
        )

        output = core.CfnOutput(
            self,
            "MyOutput1",
            value=mybuck.bucket_name,
            description=f"My First  CDK Bucker",
            export_name="MyOutput1"

        )