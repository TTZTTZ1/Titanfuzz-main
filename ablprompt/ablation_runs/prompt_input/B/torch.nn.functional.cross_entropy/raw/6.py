import torch
import torch.nn.functional as F

# Example inputs
logits = torch.randn(4, 5, requires_grad=True)
targets = torch.tensor([1, 0, 4, 3])

# Compute cross-entropy loss
loss = F.cross_entropy(logits, targets, weight=torch.tensor([0.1, 0.2, 0.3, 0.4, 0.5]), ignore_index=0)

print(loss)