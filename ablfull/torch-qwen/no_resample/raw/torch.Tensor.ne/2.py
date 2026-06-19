import torch

# Generate input data
tensor = torch.tensor([1, 2, 3])
other = torch.tensor([1, 0, 3])

# Call the API
result = tensor.ne(other)
print(result)