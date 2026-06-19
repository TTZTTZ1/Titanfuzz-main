import torch

# Generate valid input data
x = torch.tensor([[1, 2], [3, 4]])

# Call the API torch.transpose
result = torch.transpose(x, 0, 1)
print(result)