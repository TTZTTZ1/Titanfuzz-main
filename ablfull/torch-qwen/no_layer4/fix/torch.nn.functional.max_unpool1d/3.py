import torch
input_tensor = torch.randn(1, 16)
indices = torch.tensor([[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]])
kernel_size = 2
output = torch.nn.functional.max_unpool1d(input_tensor, indices, kernel_size=kernel_size)