import torch
import torch.nn.functional as F

# Create some dummy data
input = torch.randn(3, requires_grad=True)
target = torch.empty(3).random_(2)

# Compute binary cross-entropy loss
loss = F.binary_cross_entropy(input, target.float())

print(loss)