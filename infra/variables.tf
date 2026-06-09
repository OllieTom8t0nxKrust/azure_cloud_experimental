variable "region" {
  default = "sa-east-1"
}

variable "instance_type" {
  default = "t2.micro"
}

variable "ami_id" {
  description = "Debian free tier x86_64 AMI"
  default     = "ami-0a667c9e0dcad4277"
}

variable "volume_size" {
  default = 150
}

variable "key_name" {
  description = "The name of the SSH key pair"
  default     = "HUNTING-KEY"
}