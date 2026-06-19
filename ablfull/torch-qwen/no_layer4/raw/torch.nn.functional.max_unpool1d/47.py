import torch

input_tensor = torch.randn(1, 16)
indices = torch.arange(16, dtype=torch.long).unsqueeze(0)
kernel_size = 2

output = torch.nn.functional.max_unpool1d(input_tensor, indices, kernel_size=kernel_size)