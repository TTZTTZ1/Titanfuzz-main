import torch

# Generate valid input data
tensor = torch.tensor([[1, 0], [0, 2]])

# Call the API
result = tensor.nonzero(as_tuple=True)

print(result)