import torch

input_tensor = torch.randn(1, 16)
indices = torch.tensor([[[0, 1, 2, 3]]])
kernel_size = 2
stride = 2
padding = 0
output_size = None

result = torch.nn.functional.max_unpool1d(input_tensor, indices, kernel_size, stride, padding, output_size)