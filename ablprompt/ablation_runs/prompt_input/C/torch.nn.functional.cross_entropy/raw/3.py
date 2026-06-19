import torch
import torch.nn.functional as F

# Example logits tensor (batch_size=4, num_classes=5)
logits = torch.randn(4, 5)

# Example target tensor (batch_size=4)
targets = torch.tensor([0, 2, 1, 3])

# Compute cross-entropy loss
loss = F.cross_entropy(logits, targets, weight=torch.tensor([0.8, 0.7, 1.0, 1.2, 1.1]), ignore_index=-100, reduction='mean', label_smoothing=0.1)

print(loss.item())