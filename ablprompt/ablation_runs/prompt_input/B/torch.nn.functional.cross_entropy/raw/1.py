import torch
import torch.nn.functional as F

# Example input tensor with shape (batch_size, num_classes)
input = torch.randn(3, 5, requires_grad=True)

# Example target tensor with shape (batch_size)
target = torch.tensor([1, 4, 0])

# Compute cross-entropy loss
loss = F.cross_entropy(input, target, weight=torch.tensor([0.2, 0.8, 1.0, 1.0, 1.0]), ignore_index=0, reduction='mean', label_smoothing=0.1)

print(loss)