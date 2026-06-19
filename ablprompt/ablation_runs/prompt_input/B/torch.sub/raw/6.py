import torch

# Create two tensors of different shapes but compatible due to broadcasting
a = torch.tensor([[1, 2], [3, 4]], dtype=torch.float32)
b = torch.tensor([0, 1], dtype=torch.float32)

# Perform element-wise subtraction with alpha=2
result = torch.sub(a, b, alpha=2)

print(result)