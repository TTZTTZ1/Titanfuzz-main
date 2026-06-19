import torch

input_data = torch.randn(1, 4, 5)
indices = torch.tensor([[[0, 2, 2, 0, 1]]])
kernel_size = 2
stride = None
padding = 0
output_size = None

result = torch.nn.functional.max_unpool1d(input_data, indices, kernel_size, stride, padding, output_size)
print(result)