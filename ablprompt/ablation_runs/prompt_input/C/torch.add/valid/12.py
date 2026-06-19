import torch

# Create two tensors
a = torch.tensor([[1, 2], [3, 4]], dtype=torch.float32)
b = torch.tensor([[0.5, 0.5], [0.5, 0.5]], dtype=torch.float32)

# Perform element-wise addition with alpha scaling
result = torch.add(a, b, alpha=2)

print(result)