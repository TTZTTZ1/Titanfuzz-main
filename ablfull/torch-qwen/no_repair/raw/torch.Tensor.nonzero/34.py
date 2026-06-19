import torch

# Prepare valid input data
tensor = torch.tensor([[0, 0], [0, 2]])

# Call the API
result = tensor.nonzero(as_tuple=True)

print(result)