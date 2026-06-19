import torch
import torch.nn.functional as F

# Create random logits tensor with shape (batch_size, num_classes)
logits = torch.randn(32, 10)

# Create target tensor with shape (batch_size)
targets = torch.randint(0, 10, (32,))

# Calculate cross-entropy loss
loss = F.cross_entropy(logits, targets, weight=None, ignore_index=-100, reduction='mean', label_smoothing=0.1)

print(f"Cross-Entropy Loss: {loss.item()}")