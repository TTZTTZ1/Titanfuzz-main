import torch
import torch.nn.functional as F

# Create random logits and target tensors
logits = torch.randn(5, 3)
targets = torch.randint(0, 3, (5,))

# Compute cross-entropy loss with class weighting and label smoothing
weight = torch.tensor([0.1, 0.8, 0.1])
label_smoothing = 0.1
loss = F.cross_entropy(logits, targets, weight=weight, label_smoothing=label_smoothing)

print(loss)