import torch

# Task 2: Generate input data
input_tensor = torch.tensor(-float('inf'))

# Task 3: Call the API
result = torch.isneginf(input_tensor)
print(result)