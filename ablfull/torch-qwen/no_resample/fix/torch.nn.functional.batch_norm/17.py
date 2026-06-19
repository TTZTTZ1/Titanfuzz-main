import torch
input_tensor = torch.randn(10, 3, 224, 224)
running_mean = torch.zeros(3)
running_var = torch.ones(3)
weight = torch.ones(3)
bias = torch.zeros(3)
training = True
momentum = 0.1
eps = 1e-05
output_tensor = torch.nn.functional.batch_norm(input=input_tensor, running_mean=running_mean, running_var=running_var, weight=weight, bias=bias, training=training, momentum=momentum, eps=eps)