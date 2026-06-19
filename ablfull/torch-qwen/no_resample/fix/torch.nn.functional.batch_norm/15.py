import torch
input_data = torch.randn(10, 3, 32, 32, dtype=torch.float32)
running_mean = torch.zeros(3, dtype=torch.float32)
running_var = torch.ones(3, dtype=torch.float32)
output = torch.nn.functional.batch_norm(input_data, running_mean, running_var)