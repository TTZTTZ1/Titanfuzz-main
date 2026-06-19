import torch

# Generate input data
tensor = torch.rand(4)

# Call the API
result = tensor.bernoulli_()

print(result)