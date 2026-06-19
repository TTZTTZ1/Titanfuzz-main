import torch

# Generate input data
a = torch.tensor([[1, 2], [3, 4]])

# Call the API
result = torch.transpose(a, 0, 1)
print(result)