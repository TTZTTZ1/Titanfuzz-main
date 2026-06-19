
import torch
input_data = torch.randn(3, 4)
running_mean = torch.zeros(4)
running_var = torch.ones(4)
output = torch.nn.functional.batch_norm(input_data, running_mean, running_var)
