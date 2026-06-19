import torch
import torch.nn.functional as F

# Create random logits and target tensors
logits = torch.randn(10, 5)
targets = torch.randint(0, 5, (10,))

# Compute cross-entropy loss with class weighting, ignoring index -1, and mean reduction
class_weights = torch.tensor([0.1, 0.2, 0.3, 0.2, 0.2])
loss = F.cross_entropy(logits, targets, weight=class_weights, ignore_index=-1, reduction='mean')

print(loss)