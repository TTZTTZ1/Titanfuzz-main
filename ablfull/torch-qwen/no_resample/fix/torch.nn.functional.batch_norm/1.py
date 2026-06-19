import torch
input_data = torch.randn(32, 10)
running_mean = torch.zeros(10)
running_var = torch.ones(10)
output = torch.nn.functional.batch_norm(input_data, running_mean, running_var)