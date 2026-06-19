import torch

# Example usage of torch.where
x = torch.tensor([1, 2, 3])
y = torch.tensor([4, 5, 6])
condition = x > y
result = torch.where(condition, x, y)
print(result)  # Output will be tensor([4, 5, 6])