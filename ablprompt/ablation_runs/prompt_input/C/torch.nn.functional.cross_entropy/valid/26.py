import torch
import torch.nn.functional as F

# Example input tensor of shape (batch_size, num_classes)
logits = torch.randn(5, 3, requires_grad=True)

# Example target tensor of shape (batch_size)
targets = torch.randint(0, 3, (5,))

# Compute cross-entropy loss
loss = F.cross_entropy(logits, targets, weight=torch.tensor([0.5, 1.0, 1.5]), reduction='mean', label_smoothing=0.1)

print(loss)