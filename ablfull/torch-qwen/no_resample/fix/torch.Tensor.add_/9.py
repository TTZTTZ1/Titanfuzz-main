import torch
tensor = torch.tensor([1.0, 2.0, 3.0], dtype=torch.float)
other = torch.tensor([4.0, 5.0, 6.0], dtype=torch.float)
alpha = 2.0
result = tensor.add_(other, alpha=alpha)
print(result)