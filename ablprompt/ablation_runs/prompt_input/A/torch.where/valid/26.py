import torch

# Create two tensors
x = torch.tensor([1, 2, 3])
y = torch.tensor([4, 5, 6])

# Use torch.where to select elements from x or y based on a condition
condition = (x > y)
result = torch.where(condition, x, y)

print(result)  # Output will be tensor([4, 5, 6]) since x is not greater than y in any position