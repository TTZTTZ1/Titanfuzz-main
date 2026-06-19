import torch
import torch.nn.functional as F

# Example tensor of logits
logits = torch.randn(5, 3)

# Example tensor of integer class labels
labels = torch.tensor([1, 0, 2, 1, 0])

# Compute cross-entropy loss
loss = F.cross_entropy(logits, labels)

print(f"Cross-Entropy Loss: {loss.item()}")