import torch
import torch.nn.functional as F

# Example input and target tensors
input = torch.tensor([0.1, 0.4, 0.35], requires_grad=True)
target = torch.tensor([0, 1, 0])

# Compute binary cross-entropy loss
loss = F.binary_cross_entropy(input, target)

print(f"Loss: {loss.item()}")