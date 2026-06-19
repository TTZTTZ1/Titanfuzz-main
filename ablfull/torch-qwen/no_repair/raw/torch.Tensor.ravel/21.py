import torch

# Generate input data
input_tensor = torch.tensor([[1, 2], [3, 4]])

# Call the API
flattened_tensor = input_tensor.ravel()

print(flattened_tensor)