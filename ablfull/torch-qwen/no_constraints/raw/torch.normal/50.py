import torch

mean = 0.0
std_dev = 1.0
size = (2, 3)
input_data = torch.randn(size)

output = torch.normal(mean, std_dev, size, out=input_data)