import aws_cdk as core
import aws_cdk.assertions as assertions

from demo_devops_aws.demo_devops_aws_stack import DemoDevopsAwsStack

# example tests. To run these tests, uncomment this file along with the example
# resource in demo_devops_aws/demo_devops_aws_stack.py
def test_sqs_queue_created():
    app = core.App()
    stack = DemoDevopsAwsStack(app, "demo-devops-aws")
    template = assertions.Template.from_stack(stack)

#     template.has_resource_properties("AWS::SQS::Queue", {
#         "VisibilityTimeout": 300
#     })
