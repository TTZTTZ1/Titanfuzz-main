import torch
import torch.nn.functional as F

# Example logits tensor (batch_size=4, num_classes=5)
logits = torch.randn(4, 5)

# Example target tensor (batch_size=4)
targets = torch.randint(0, 5, (4,))

# Compute cross-entropy loss
loss = F.cross_entropy(logits, targets, weight=None, size_average=None, ignore_index=-100, reduce=None, reduction='mean', label_smoothing=0.0)

print(loss)