import torch
input_data = torch.randn(32, 3, 28, 28)
running_mean = torch.zeros(3)
running_var = torch.ones(3)
output = torch.nn.functional.batch_norm(input_data, running_mean, running_var)