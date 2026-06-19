import torch

# Generate input data
data = torch.tensor([0, 1, 0, 2])

# Call the API
result = data.nonzero(as_tuple=True)

print(result)