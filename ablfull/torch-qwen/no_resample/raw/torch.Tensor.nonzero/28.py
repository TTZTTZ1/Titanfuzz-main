import torch

# Prepare valid input data
tensor = torch.tensor([[0, 0], [0, 1]])

# Call the API
result = tensor.nonzero(as_tuple=True)

print(result)