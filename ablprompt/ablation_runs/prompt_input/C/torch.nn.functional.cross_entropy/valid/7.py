import torch
import torch.nn.functional as F

# Example input tensor of shape (batch_size, num_classes)
logits = torch.randn(10, 5)

# Example target tensor of shape (batch_size)
targets = torch.randint(0, 5, (10,))

# Compute cross-entropy loss
loss = F.cross_entropy(logits, targets, weight=torch.tensor([0.1, 0.4, 0.6, 0.8, 1.0]), ignore_index=2, reduction='mean', label_smoothing=0.1)

print(f"Cross-Entropy Loss: {loss.item()}")