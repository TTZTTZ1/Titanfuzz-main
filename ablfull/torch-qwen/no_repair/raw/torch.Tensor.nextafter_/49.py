import torch

# Create input tensors of the same type
a = torch.tensor([1.0, 2.0], dtype=torch.float32)
b = torch.tensor([1.1, 2.2], dtype=torch.float32)

# Call the target API
result = torch.Tensor.nextafter(a, b)