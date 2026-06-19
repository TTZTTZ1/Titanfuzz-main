import torch

# Generate input data
tensor = torch.tensor([[0, 1], [2, 0]], dtype=torch.int)

# Call the API
result = tensor.nonzero(as_tuple=True)