import torch
import torch.nn.functional as F

# Example input tensor with shape (batch_size, num_classes)
logits = torch.randn(4, 5)

# Example target tensor with shape (batch_size)
targets = torch.tensor([0, 2, 1, 4])

# Compute cross-entropy loss
loss = F.cross_entropy(logits, targets, weight=torch.tensor([0.1, 0.2, 0.3, 0.4, 0.5]), reduction='mean')

print(loss.item())