import torch

# Task 2: Generate input data
input_data = torch.tensor([[1, 2], [3, 4]])

# Task 3: Call the API torch.Tensor.ravel
flattened_data = input_data.ravel()

print(flattened_data)