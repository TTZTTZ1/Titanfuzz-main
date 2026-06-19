import torch
input_tensor = torch.randn(1, 64, 6)
indices = torch.randint(0, 6, (1, 64, 6))
kernel_size = 3
padding = 1
output = torch.nn.functional.max_unpool1d(input_tensor, indices, kernel_size, padding=padding)