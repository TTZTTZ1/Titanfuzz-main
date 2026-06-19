import torch

# Task 2: Generate input data
input_tensor = torch.randn(1, 4, 5)
indices = torch.tensor([[[0, 1, 2, 3, 4]]])
kernel_size = 2
stride = 2
padding = 0
output_size = None

# Task 3: Call the API
output_tensor = torch.nn.functional.max_unpool1d(input_tensor, indices, kernel_size, stride, padding, output_size)

print(output_tensor)