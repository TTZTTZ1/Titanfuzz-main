import torch

input_tensor = torch.randn(1, 16)
indices = torch.argmax(input_tensor, dim=1, keepdim=True)
kernel_size = 2
stride = 2
padding = 0

output = torch.nn.functional.max_unpool1d(input_tensor, indices, kernel_size, stride, padding)