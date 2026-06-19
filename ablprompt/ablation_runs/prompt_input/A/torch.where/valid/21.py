import torch

# Example usage of torch.where
condition = torch.tensor([True, False, True])
x = torch.tensor([1, 2, 3])
y = torch.tensor([4, 5, 6])

result = torch.where(condition, x, y)
print(result)  # Output: tensor([1, 5, 3])