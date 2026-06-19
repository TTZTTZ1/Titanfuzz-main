import torch

input_data = torch.randn(1, 3, 4, 5, 6)
padding = (1, 2, 3, 4, 5, 6)
output = torch.nn.functional.pad(input_data, pad=padding, mode='reflect')