import torch

# Task 2: Generate input data
input_data = torch.tensor([[1, 2], [3, 4]])

# Task 3: Call the API torch.flatten
flattened_data = torch.flatten(input_data)

print(flattened_data)