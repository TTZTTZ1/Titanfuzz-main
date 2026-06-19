import torch

# Generate input data
tensor = torch.tensor([1.0, 2.0, 3.0])
other = torch.tensor([1.0, 2.5, 3.0])

# Call the API
result = tensor.ne(other)
print(result)