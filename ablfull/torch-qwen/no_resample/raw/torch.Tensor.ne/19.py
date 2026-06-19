import torch

# Prepare input data
tensor = torch.tensor([1, 2, 3], dtype=torch.int)
other = torch.tensor([1, 0, 3], dtype=torch.int)

# Call the API
result = tensor.ne(other)
print(result)