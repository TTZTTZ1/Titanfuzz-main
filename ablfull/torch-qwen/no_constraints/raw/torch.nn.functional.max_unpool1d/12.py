import torch

# Task 2: Generate input data
input_tensor = torch.randn(1, 4, 6)
indices = torch.tensor([[[0, 1, 2, 3, 4, 5]]])
kernel_size = 2
stride = 2
padding = 0
output_size = (1, 4, 12)

# Task 3: Call the API
result = torch.nn.functional.max_unpool1d(input_tensor, indices, kernel_size, stride, padding, output_size)
print(result)