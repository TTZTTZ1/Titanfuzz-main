import torch

# Task 2: Generate input data
input_tensor = torch.tensor([float('-inf'), -2.0, 0.0, 2.0])

# Task 3: Call the API
result = torch.isneginf(input_tensor)

print(result)