import torch
import torch.nn.functional as F

# Create random logits and target tensors
logits = torch.randn(5, 3)
target = torch.randint(0, 3, (5,))

# Compute cross-entropy loss
loss = F.cross_entropy(logits, target, weight=torch.tensor([0.1, 0.8, 0.1]), ignore_index=2, reduction='mean', label_smoothing=0.1)

print(loss)