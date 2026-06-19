import torch
import torch.nn.functional as F

# Example inputs
logits = torch.randn(4, 5)  # Batch of 4 samples, each with 5 classes
targets = torch.tensor([1, 0, 4, 2])  # Target class indices

# Compute cross-entropy loss
loss = F.cross_entropy(logits, targets)

print(loss)