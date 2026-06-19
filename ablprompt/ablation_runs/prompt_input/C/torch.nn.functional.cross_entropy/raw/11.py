import torch
import torch.nn.functional as F

# Example logits tensor for 5 classes and 3 samples
logits = torch.randn(3, 5)

# Example target tensor with class indices
targets = torch.tensor([0, 2, 4])

# Compute cross-entropy loss
loss = F.cross_entropy(logits, targets, weight=torch.tensor([0.1, 0.2, 0.3, 0.4, 0.5]), ignore_index=2, reduction='sum')

print(loss)