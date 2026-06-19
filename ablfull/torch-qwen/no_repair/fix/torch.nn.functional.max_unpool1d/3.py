
import torch
input_tensor = torch.randn(1, 16)
indices_tensor = torch.tensor([[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]])
kernel_size = 2
stride = 2
padding = 0
output_size = (32,)
result = torch.nn.functional.max_unpool1d(input_tensor, indices_tensor, kernel_size, stride, padding, output_size)
