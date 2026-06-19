import torch

# Task 2: Generate input data
input_tensor = torch.randn(1, 3, 4, 5, 6)

# Task 3: Call the API
output_tensor = torch.nn.functional.avg_pool3d(input_tensor, kernel_size=2)