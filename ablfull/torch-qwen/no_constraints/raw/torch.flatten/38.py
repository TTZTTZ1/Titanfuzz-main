import torch

# Task 2: Generate input data
input_tensor = torch.tensor([[1.0, 2.0], [3.0, 4.0]])

# Task 3: Call the API torch.flatten
flattened_tensor = torch.flatten(input_tensor)
print(flattened_tensor)