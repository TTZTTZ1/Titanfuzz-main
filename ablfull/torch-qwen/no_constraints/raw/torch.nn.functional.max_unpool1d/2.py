import torch

# Task 2: Generate input data
input_tensor = torch.randn(1, 16)
indices = torch.tensor([[[0], [1], [2], [3], [4], [5], [6], [7], [8], [9], [10], [11], [12], [13], [14], [15]]])
kernel_size = 2
stride = 2

# Task 3: Call the API
output_tensor = torch.nn.functional.max_unpool1d(input_tensor, indices, kernel_size, stride)

print(output_tensor)