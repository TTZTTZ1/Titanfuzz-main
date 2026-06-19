import torch

# Prepare input data
input_tensor = torch.tensor([[[1.0, 2.0, 3.0], [4.0, 5.0, 6.0]]])
indices = torch.tensor([[[0, 1, 2], [3, 4, 5]]])
kernel_size = 2
stride = None
padding = 0
output_size = None

# Call the API
result = torch.nn.functional.max_unpool1d(input_tensor, indices, kernel_size, stride, padding, output_size)
print(result)