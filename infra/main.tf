provider "aws" {
  region = var.region
}

data "aws_iam_role" "existing_ec2_role" {
  name = "hunting-machine-instance-role"
}

data "aws_iam_instance_profile" "existing_instance_profile" {
  name = "HUNTING-MACHINE"
}

resource "aws_instance" "debian_instance" {
  ami                  = var.ami_id
  instance_type        = var.instance_type
  key_name             = "HUNTING-KEY"
  iam_instance_profile = data.aws_iam_instance_profile.existing_instance_profile.name

  root_block_device {
    volume_size = var.volume_size
    volume_type = "gp3"
  }

  tags = {
    Name = "HUNTING-MACHINE"
  }
}
