from aws_cdk import (
    Stack,
    aws_ec2 as ec2,
    aws_ecs as ecs,
    aws_ecs_patterns as ecs_patterns,
    aws_ecr as ecr,
    aws_iam as iam,
)
from constructs import Construct

class DemoDevopsAwsStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        docker_tag = self.node.try_get_context("docker_tag")
        mongodb_uri = self.node.try_get_context("mongodb_uri")

        vpc = ec2.Vpc.from_lookup(self, "VPC",
            is_default=True
        )

        cluster = ecs.Cluster(
            self,
            "EcsCluster",
            vpc=vpc,
        )

        ecr_repository = ecr.Repository.from_repository_name(
            self,
            "EcrRepository",
            "demo-devops-aws",
        )

        ecs_task_role = iam.Role(
            self,
            "EcsTaskRole",
            assumed_by=iam.ServicePrincipal("ecs-tasks.amazonaws.com"),
            description="Grant access to multiple AWS services",
        )

        ecr_image = ecs.ContainerImage.from_ecr_repository(
            ecr_repository,
            docker_tag,
        )

        fargate_cluster = ecs_patterns.ApplicationLoadBalancedFargateService(
            self,
            "FargateService",
            cluster=cluster,
            memory_limit_mib=1024,
            cpu=512,
            desired_count=1,
            task_image_options=ecs_patterns.ApplicationLoadBalancedTaskImageOptions(
                image=ecr_image,
                task_role=ecs_task_role,
                environment={
                    "MONGODB_URI": mongodb_uri,
                },
            ),
        )

        fargate_cluster.target_group.configure_health_check(
            path="/healthcheck"
        )
