import torch

# Task 2: Generate input data
input_tensor = torch.randn(1, 5, 4)
indices = torch.tensor([[[0], [1], [2], [3]]])
kernel_size = 2
stride = None
padding = 0
output_size = None

# Task 3: Call the API
result = torch.nn.functional.max_unpool1d(input_tensor, indices, kernel_size, stride, padding, output_size)

print(result)