import torch

# Create two tensors
a = torch.tensor([[1, 2], [3, 4]], dtype=torch.float32)
b = torch.tensor([[0.5, -1.0], [1.5, -2.0]], dtype=torch.float32)

# Perform element-wise addition with scaling factor alpha
result = torch.add(a, b, alpha=2)

print(result)