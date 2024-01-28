provider "aws" {
  region = "il-central-1"
}

resource "aws_launch_configuration" "psifas" {
  name          = "psifas_config"

  image_id      = "ami-0de006b72d983a5a5"
  instance_type = "t3.micro"

  lifecycle {
    create_before_destroy = true
  }
}

resource "aws_autoscaling_group" "psifas" {
  name                 = "psifas_asg"
  desired_capacity     = 1
  max_size             = 10
  min_size             = 1
  health_check_type    = "EC2"
  force_delete         = true
  
  vpc_zone_identifier  = ["subnet-05fb22ce3ba0d2ec0", "subnet-0f01897213d3af370", "subnet-0f18fe089c34b0441"] 
  launch_configuration = aws_launch_configuration.psifas.id

  tag {
    key                 = "Name"
    value               = "psifas-asg"
    propagate_at_launch = true
  }

  health_check_grace_period = 300  # Adjust as needed

  lifecycle {
    create_before_destroy = true
  }
}

resource "aws_autoscaling_policy" "cpu-scaling" {
  name                      = "cpu-scaling"
  scaling_adjustment        = 1
  cooldown                  = 300  # Adjust as needed
  adjustment_type           = "ChangeInCapacity"


  target_tracking_configuration {
    predefined_metric_specification {
      predefined_metric_type = "ASGAverageCPUUtilization"
    }

    target_value = 50.0
  }

  autoscaling_group_name = aws_autoscaling_group.psifas.name
}
