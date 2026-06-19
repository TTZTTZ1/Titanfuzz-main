import torch

# Generate input data
input_tensor = torch.randn(1, 3, 4)
indices_tensor = torch.tensor([[[1, 0, 2, 1]]])
kernel_size = 2
stride = None
padding = 0
output_size = None

# Call the API
result = torch.nn.functional.max_unpool1d(input_tensor, indices_tensor, kernel_size, stride, padding, output_size)