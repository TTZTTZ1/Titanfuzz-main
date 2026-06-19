import torch

# Create some tensors
tensor1 = torch.tensor([1, 2, 3])
tensor2 = torch.tensor([4, 5, 6])

# Stack them along a new dimension
stacked_tensor = torch.stack((tensor1, tensor2), dim=0)

print(stacked_tensor)