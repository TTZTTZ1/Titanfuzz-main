import torch
import torch.nn.functional as F

# Example input and target tensors
input_probs = torch.tensor([[0.9, 0.1], [0.4, 0.6]])
targets = torch.tensor([[1.0, 0.0], [0.0, 1.0]])

# Compute binary cross-entropy loss
loss = F.binary_cross_entropy(input_probs, targets, reduction='mean')

print(f"Computed Loss: {loss.item()}")