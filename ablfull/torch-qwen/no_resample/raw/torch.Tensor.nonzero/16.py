import torch

# Generate input data
tensor = torch.tensor([[0, 1], [2, 0]])

# Call the API
result = tensor.nonzero(as_tuple=True)

print(result)