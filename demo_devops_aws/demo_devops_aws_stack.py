from aws_cdk import (
    Stack,
    aws_ec2 as ec2,
    aws_ecs as ecs,
)
from constructs import Construct

class DemoDevopsAwsStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        vpc = ec2.Vpc.from_lookup(self, "VPC",
            is_default=True
        )

        cluster = ecs.Cluster(
            self,
            "EcsCluster",
            vpc=vpc,
        )
