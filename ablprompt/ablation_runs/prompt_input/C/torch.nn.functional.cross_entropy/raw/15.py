import torch
import torch.nn.functional as F

# Example input tensor (logits)
logits = torch.randn(4, 5)

# Example target tensor (class indices)
targets = torch.tensor([1, 0, 4, 2])

# Compute cross-entropy loss
loss = F.cross_entropy(logits, targets, weight=torch.tensor([0.8, 0.7, 0.6, 0.9, 0.5]), reduction='mean', label_smoothing=0.1)

print(f"Cross-Entropy Loss: {loss.item()}")