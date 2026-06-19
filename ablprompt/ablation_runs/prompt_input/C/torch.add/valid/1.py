import torch

# Create two tensors
a = torch.tensor([[1, 2], [3, 4]], dtype=torch.float32)
b = torch.tensor([[5, 6], [7, 8]], dtype=torch.float32)

# Use torch.add to perform element-wise addition with a scaling factor
result = torch.add(a, b, alpha=2)

print(result)