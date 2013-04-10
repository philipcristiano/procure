import argparse
import os

import boto.ec2
import yaml

def main():
    args = get_args()
    template = yaml.safe_load(open(args.template).read())
    validate_template(template)
    conn = boto.ec2.connect_to_region(
        template['region'],
        aws_access_key_id=os.getenv('AWS_ACCESS_KEY'),
        aws_secret_access_key=os.getenv('AWS_SECRET_KEY'),
    )

    resp = conn.run_instances(
        template['ami'],
        key_name=args.key,
        instance_type=template['instance-type'],
        placement=args.zone,
        security_groups=template['security-groups']
    )
    instance = resp.instances[0]
    conn.create_tags(instance.id, {'Name': args.name})


def validate_template(template):
    assert template['region'] == 'us-east-1'
    assert template['instance-type'] == 'm1.large'
    assert len(template['security-groups']) > 0



def get_args():
    parser = argparse.ArgumentParser(description='Spins up an EC2 instance')
    parser.add_argument('--template', type=str, help='Path to a template')
    parser.add_argument('--key', type=str, help='Key pair')
    parser.add_argument('--name', type=str, help='Node name')
    parser.add_argument('--zone', type=str, help='Availability zone within the region')
    return parser.parse_args()

if __name__ == '__main__':
    main()
