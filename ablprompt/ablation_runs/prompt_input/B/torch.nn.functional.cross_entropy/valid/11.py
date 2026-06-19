import torch
import torch.nn.functional as F

# Example input tensor with shape (batch_size, num_classes)
logits = torch.randn(5, 10)

# Example target tensor with shape (batch_size)
targets = torch.randint(0, 10, (5,))

# Compute cross-entropy loss
loss = F.cross_entropy(logits, targets, weight=torch.tensor([0.5, 1.0, 1.5, 2.0, 2.5, 3.0, 3.5, 4.0, 4.5, 5.0]), reduction='mean')

print(loss)