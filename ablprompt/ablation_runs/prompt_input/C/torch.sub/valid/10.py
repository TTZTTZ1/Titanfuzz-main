import torch

# Create two tensors
a = torch.tensor([[1, 2], [3, 4]], dtype=torch.float32)
b = torch.tensor([[5, 6], [7, 8]], dtype=torch.float32)

# Perform element-wise subtraction with alpha=0.5
result = torch.sub(a, b, alpha=0.5)

print(result)