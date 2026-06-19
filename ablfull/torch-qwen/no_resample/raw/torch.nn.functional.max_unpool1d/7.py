import torch

input_tensor = torch.randn(1, 3, 4)
indices = torch.tensor([[[0, 1, 2, 3]]])
kernel_size = 2
stride = None
padding = 0
output_size = None

result = torch.nn.functional.max_unpool1d(input_tensor, indices, kernel_size, stride, padding, output_size)