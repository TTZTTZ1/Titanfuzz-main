import torch
(N, C) = (2, 3)
input_data = torch.randn(N, C)
running_mean = torch.zeros(C)
running_var = torch.ones(C)
weight = torch.ones(C)
bias = torch.zeros(C)
output = torch.nn.functional.batch_norm(input_data, running_mean, running_var, weight, bias, training=True)