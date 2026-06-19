import torch

# Create some tensors
x = torch.tensor([1, 2, 3])
y = torch.tensor([4, 5, 6])

# Use torch.where to conditionally select elements from x and y
condition = (x > 2)
result = torch.where(condition, x, y)

print(result)  # Output will be tensor([4, 5, 3])