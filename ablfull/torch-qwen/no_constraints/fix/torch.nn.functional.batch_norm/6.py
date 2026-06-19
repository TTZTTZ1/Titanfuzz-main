import torch
input_tensor = torch.randn(3, 4, 5)
running_mean = torch.zeros(4)
running_var = torch.ones(4)
weight = torch.ones(4)
bias = torch.zeros(4)
output_tensor = torch.nn.functional.batch_norm(input_tensor, running_mean, running_var, weight, bias, True)