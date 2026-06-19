import torch

# Create two tensors
a = torch.tensor([[1, 2], [3, 4]], dtype=torch.float)
b = torch.tensor([[5, 6], [7, 8]], dtype=torch.float)

# Perform element-wise addition with scaling
result = torch.add(a, b, alpha=0.5)

print(result)