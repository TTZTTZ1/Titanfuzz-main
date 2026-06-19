import torch
import torch.nn.functional as F

# Example input tensor (logits)
logits = torch.tensor([[2.0, 1.0, 0.1], [0.5, 2.0, 0.3]])

# Example target tensor (class indices)
targets = torch.tensor([0, 2])

# Compute cross-entropy loss
loss = F.cross_entropy(logits, targets, weight=torch.tensor([0.5, 1.0, 2.0]), ignore_index=-1)

print(loss)