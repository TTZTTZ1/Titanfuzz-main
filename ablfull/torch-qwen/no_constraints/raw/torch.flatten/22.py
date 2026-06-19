import torch

# Task 2: Generate input data
input_tensor = torch.tensor([[1, 2], [3, 4]])

# Task 3: Call the API torch.flatten
flattened_tensor = torch.flatten(input_tensor)

print(flattened_tensor)