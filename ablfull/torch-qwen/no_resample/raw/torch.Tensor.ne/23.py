import torch

# Generate input data
a = torch.tensor([1, 2, 3], dtype=torch.float)
b = 2

# Call the API
result = a.ne(b)

print(result)