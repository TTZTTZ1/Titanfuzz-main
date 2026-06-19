import torch

# Generate input data
x = torch.tensor([4.0], dtype=torch.float32)
y = torch.tensor([2.0], dtype=torch.float32)

# Call the API
result = torch.divide(x, y)
print(result)