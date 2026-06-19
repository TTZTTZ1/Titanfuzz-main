import torch
import torch.nn.functional as F

# Example inputs
logits = torch.randn(5, 3)  # Batch of 5 samples, each with 3 classes
targets = torch.randint(0, 3, (5,))  # Targets are class indices

# Compute cross-entropy loss
loss = F.cross_entropy(logits, targets, weight=torch.tensor([0.1, 0.9, 0.8]), reduction='mean', label_smoothing=0.1)

print(f"Cross-Entropy Loss: {loss.item()}")