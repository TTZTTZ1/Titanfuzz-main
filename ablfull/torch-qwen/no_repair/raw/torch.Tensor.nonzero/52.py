import torch

# Generate input data
input_tensor = torch.tensor([0, 1, 2])

# Call the API
result = input_tensor.nonzero(as_tuple=True)

print(result)