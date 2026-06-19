import torch
import torch.nn.functional as F

# Example input and target tensors
logits = torch.randn(3, 5, requires_grad=True)
targets = torch.tensor([1, 0, 4])

# Compute cross-entropy loss
loss = F.cross_entropy(logits, targets, weight=torch.tensor([0.8, 1.0, 1.2, 1.4, 1.6]), reduction='mean')

print(loss)