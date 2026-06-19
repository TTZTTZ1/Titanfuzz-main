import torch

# Generate input data
x = torch.tensor([1.0, 2.0, 3.0], dtype=torch.float32)
y = torch.tensor([4.0, 5.0, 6.0], dtype=torch.float32)

# Call the API
result = x.add_(y)
print(result)