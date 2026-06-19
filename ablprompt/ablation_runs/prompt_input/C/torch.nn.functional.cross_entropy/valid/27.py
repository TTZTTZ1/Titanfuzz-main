import torch
import torch.nn.functional as F

# Example logits tensor (batch_size=3, num_classes=5)
logits = torch.randn(3, 5)

# Example target tensor (batch_size=3)
targets = torch.tensor([1, 0, 4])

# Compute cross-entropy loss
loss = F.cross_entropy(logits, targets)

print(f"Cross-Entropy Loss: {loss.item()}")