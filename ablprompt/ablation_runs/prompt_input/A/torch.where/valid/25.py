import torch

# Example usage of torch.where
condition = torch.tensor([True, False, True])
x = torch.tensor([10, 20, 30])
y = torch.tensor([40, 50, 60])

result = torch.where(condition, x, y)
print(result)  # Output: tensor([10, 50, 30])