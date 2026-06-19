import torch
import torch.nn.functional as F

# Example input tensor of shape (batch_size, num_classes)
logits = torch.tensor([[2.0, 1.0, 0.1], [0.5, 2.0, 0.3]])

# Example target tensor of shape (batch_size)
targets = torch.tensor([0, 1])

# Compute cross-entropy loss
loss = F.cross_entropy(logits, targets)

print(loss.item())