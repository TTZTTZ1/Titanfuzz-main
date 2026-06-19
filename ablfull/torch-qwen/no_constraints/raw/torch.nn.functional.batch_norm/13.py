import torch

input_tensor = torch.randn(10, 64, 32, 32)
running_mean = torch.zeros(64)
running_var = torch.ones(64)
weight = torch.ones(64)
bias = torch.zeros(64)

output_tensor = torch.nn.functional.batch_norm(input_tensor, running_mean, running_var, weight, bias, training=True)