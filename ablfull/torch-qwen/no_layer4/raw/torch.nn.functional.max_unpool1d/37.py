import torch

# Prepare input data
input_tensor = torch.randn(1, 4, 5)
indices = torch.tensor([[[0], [2], [3]]])
kernel_size = 2
stride = None
padding = 0
output_size = None

# Call the API
result = torch.nn.functional.max_unpool1d(input_tensor, indices, kernel_size, stride, padding, output_size)