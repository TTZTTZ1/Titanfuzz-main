import torch
from torch.nn.functional import binary_cross_entropy

# Example tensors
input_probs = torch.tensor([0.1, 0.4, 0.35], requires_grad=True)
targets = torch.tensor([0, 1, 1])

# Compute binary cross-entropy loss
loss = binary_cross_entropy(input_probs, targets, reduction='mean')

print(f"Computed Loss: {loss.item()}")