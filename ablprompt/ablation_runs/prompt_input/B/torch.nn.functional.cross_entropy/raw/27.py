import torch
import torch.nn.functional as F

# Example inputs
logits = torch.tensor([[2.0, 1.0, 0.1], [0.5, 2.5, 1.0]], requires_grad=True)
targets = torch.tensor([0, 2])

# Compute cross-entropy loss
loss = F.cross_entropy(logits, targets, weight=torch.tensor([0.5, 1.0, 1.5]), reduction='mean', label_smoothing=0.1)

print(loss)