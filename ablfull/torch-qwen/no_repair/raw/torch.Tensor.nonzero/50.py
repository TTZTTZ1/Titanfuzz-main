import torch

# Generate input data
input_tensor = torch.tensor([0, 1, 0, 2], dtype=torch.long)

# Call the API
result = input_tensor.nonzero(as_tuple=True)

print(result)