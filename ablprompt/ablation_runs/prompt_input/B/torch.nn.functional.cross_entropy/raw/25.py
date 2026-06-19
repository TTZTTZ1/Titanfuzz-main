import torch
import torch.nn.functional as F

# Create some random logits and target tensors
logits = torch.randn(5, 3)
targets = torch.randint(0, 3, (5,))

# Compute cross-entropy loss with class weights, ignoring index 2, and using 'sum' reduction
class_weights = torch.tensor([0.5, 1.0, 1.5])
ignore_index = 2
reduction = 'sum'

loss = F.cross_entropy(logits, targets, weight=class_weights, ignore_index=ignore_index, reduction=reduction)

print(f"Cross-Entropy Loss: {loss.item()}")