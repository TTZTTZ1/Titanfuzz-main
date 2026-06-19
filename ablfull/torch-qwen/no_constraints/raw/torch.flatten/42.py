import torch

# Task 2: Generate input data
input_tensor = torch.randn(4, 3, 2)

# Task 3: Call the API
flattened_tensor = torch.flatten(input_tensor)
print(flattened_tensor)