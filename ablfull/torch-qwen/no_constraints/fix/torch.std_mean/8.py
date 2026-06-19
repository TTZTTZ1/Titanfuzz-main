import torch
input_data = torch.randn(5, requires_grad=True)
(std, mean) = torch.std_mean(input_data)