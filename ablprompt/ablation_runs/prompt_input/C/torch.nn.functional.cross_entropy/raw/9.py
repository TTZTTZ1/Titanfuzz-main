import torch
import torch.nn.functional as F

# Example input tensor of shape (batch_size, num_classes)
logits = torch.randn(32, 10)

# Example target tensor of shape (batch_size)
targets = torch.randint(0, 10, (32,))

# Compute cross-entropy loss
loss = F.cross_entropy(logits, targets, weight=None, size_average=None, ignore_index=-100, reduce=None, reduction='mean', label_smoothing=0.0)

print(loss)