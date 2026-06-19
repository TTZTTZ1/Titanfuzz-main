import torch
import torch.nn.functional as F

# Example inputs
logits = torch.randn(5, 3)  # Batch of 5 samples, each with 3 classes
targets = torch.tensor([1, 0, 2, 1, 0])  # Target classes for each sample

# Compute cross-entropy loss
loss = F.cross_entropy(logits, targets)

print(f"Cross-Entropy Loss: {loss.item()}")