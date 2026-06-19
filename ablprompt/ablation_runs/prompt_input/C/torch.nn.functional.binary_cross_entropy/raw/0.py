import torch
import torch.nn.functional as F

# Example input and target tensors
input_probs = torch.tensor([0.3, 0.7, 0.2], requires_grad=True)
targets = torch.tensor([0.0, 1.0, 0.0])

# Compute binary cross-entropy loss
loss = F.binary_cross_entropy(input_probs, targets)

print(f"Loss: {loss.item()}")