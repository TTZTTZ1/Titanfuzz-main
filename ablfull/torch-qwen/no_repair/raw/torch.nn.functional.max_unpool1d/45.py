import torch

input_data = torch.randn(1, 3, 5)
indices = torch.tensor([[[1, 2, 3, 4, 0]]], dtype=torch.long)
kernel_size = 2
padding = 1

output = torch.nn.functional.max_unpool1d(input_data, indices, kernel_size=kernel_size, padding=padding)