output "instance_id" {
  value = aws_instance.debian_instance.id
}

output "instance_public_ip" {
  value = aws_instance.debian_instance.public_ip
}
