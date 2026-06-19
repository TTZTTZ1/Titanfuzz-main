import torch

input_tensor = torch.randn(1, 16)
indices = torch.argmax(input_tensor, dim=1, keepdim=True).expand(-1, -1, input_tensor.size(2))
kernel_size = 2
stride = 2
padding = 0
output_size = None

result = torch.nn.functional.max_unpool1d(input_tensor, indices, kernel_size, stride, padding, output_size)