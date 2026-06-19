import torch

# Create two tensors
a = torch.tensor([[1, 2], [3, 4]], dtype=torch.float32)
b = torch.tensor([[5, 6], [7, 8]], dtype=torch.float32)

# Perform element-wise subtraction with scaling factor alpha=2
result = torch.sub(a, b, alpha=2)

print(result)