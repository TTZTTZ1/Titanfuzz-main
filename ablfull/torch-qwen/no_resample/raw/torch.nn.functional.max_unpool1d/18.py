import torch

input_tensor = torch.randn(1, 3, 5)
indices = torch.tensor([[[1, 2, 0, 4, 3]]])
kernel_size = 2
stride = 1
padding = 0
output_size = None

result = torch.nn.functional.max_unpool1d(input_tensor, indices, kernel_size, stride, padding, output_size)