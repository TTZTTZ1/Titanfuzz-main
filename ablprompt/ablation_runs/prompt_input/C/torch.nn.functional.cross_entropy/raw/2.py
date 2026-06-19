import torch
import torch.nn.functional as F

# Example inputs
logits = torch.randn(5, 3, requires_grad=True)
targets = torch.tensor([2, 0, 1, 1, 0])

# Compute cross-entropy loss
loss = F.cross_entropy(logits, targets, weight=torch.tensor([0.8, 1.0, 1.2]), reduction='mean', label_smoothing=0.1)

print(loss)