import torch
import torch.nn.functional as F

# Example input tensor with shape (batch_size, num_classes)
logits = torch.randn(5, 3)

# Example target tensor with shape (batch_size)
targets = torch.tensor([0, 1, 2, 0, 1])

# Compute cross-entropy loss
loss = F.cross_entropy(logits, targets, weight=torch.tensor([0.5, 1.0, 1.5]), ignore_index=-1, reduction='mean', label_smoothing=0.1)

print(loss)