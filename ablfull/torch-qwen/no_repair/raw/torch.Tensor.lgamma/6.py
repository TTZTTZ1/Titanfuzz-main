import torch

# Generate input data
x = torch.tensor([1.0, 2.5, 4.0])

# Call the API
result = x.lgamma()

print(result)