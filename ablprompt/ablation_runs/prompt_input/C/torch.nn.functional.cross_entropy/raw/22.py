import torch
import torch.nn.functional as F

# Example input tensor with shape (batch_size, num_classes)
input = torch.randn(5, 3)

# Example target tensor with shape (batch_size)
target = torch.tensor([0, 1, 2, 0, 1])

# Compute cross-entropy loss
loss = F.cross_entropy(input, target, weight=None, size_average=None, ignore_index=-100, reduce=None, reduction='mean', label_smoothing=0.0)

print(loss)