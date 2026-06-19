import torch

# Generate input data
x = torch.tensor([1, -2, 3])

# Call the API
result = x.negative()

print(result)