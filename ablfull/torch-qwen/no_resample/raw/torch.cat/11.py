import torch

# Generate input data
tensors = [torch.tensor([1, 2]), torch.tensor([3, 4])]
dim = 0

# Call the API
result = torch.cat(tensors, dim=dim)
print(result)