import torch
import torch.nn.functional as F

# Create random logits and targets
logits = torch.randn(5, 3)
targets = torch.randint(0, 3, (5,))

# Compute cross-entropy loss
loss = F.cross_entropy(logits, targets, weight=torch.tensor([0.5, 1.0, 1.5]), ignore_index=2, reduction='mean', label_smoothing=0.1)

print(loss)