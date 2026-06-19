import torch
import torch.nn.functional as F

# Example inputs
logits = torch.randn(3, 5, requires_grad=True)
targets = torch.tensor([1, 0, 4])

# Compute cross-entropy loss
loss = F.cross_entropy(logits, targets, weight=torch.tensor([0.1, 0.9, 0.8, 0.7, 0.6]), ignore_index=0)

print(loss)