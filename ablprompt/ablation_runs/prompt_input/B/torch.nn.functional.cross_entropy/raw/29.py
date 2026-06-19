import torch
import torch.nn.functional as F

# Create random logits and target tensors
logits = torch.randn(3, 5)
targets = torch.randint(0, 5, (3,))

# Compute cross-entropy loss
loss = F.cross_entropy(logits, targets, weight=torch.tensor([0.1, 0.2, 0.3, 0.4, 0.5]), ignore_index=4, reduction='mean', label_smoothing=0.1)

print(loss)