import torch
import torch.nn.functional as F

# Create some random logits and target tensors
logits = torch.randn(5, 3)
targets = torch.randint(0, 3, (5,))

# Compute cross-entropy loss
loss = F.cross_entropy(logits, targets)

print(loss)