import torch

# Task 2: Generate input data
input_tensor = torch.randn(1, 1, 5, 5, 5)

# Task 3: Call the API torch.nn.functional.avg_pool3d
result = torch.nn.functional.avg_pool3d(input_tensor, kernel_size=3, stride=2, padding=1)
print(result)