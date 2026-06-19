import torch
input_data = torch.randn(32, 64, 7, 7)
running_mean = torch.zeros(64)
running_var = torch.ones(64)
output = torch.nn.functional.batch_norm(input_data, running_mean, running_var)