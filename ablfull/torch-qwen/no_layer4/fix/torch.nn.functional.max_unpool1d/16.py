import torch
input_tensor = torch.randn(1, 1, 6)
indices = torch.tensor([[[1, 2, 2, 2, 2, 0]]], dtype=torch.long)
kernel_size = 2
output = torch.nn.functional.max_unpool1d(input_tensor, indices, kernel_size=kernel_size)