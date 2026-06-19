import torch

# Generate valid input data
a = torch.tensor([4.0], dtype=torch.float32)
b = torch.tensor([2.0], dtype=torch.float32)

# Call the API
result = torch.divide(a, b)

print(result)