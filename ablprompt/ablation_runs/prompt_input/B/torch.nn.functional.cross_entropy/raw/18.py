import torch
import torch.nn.functional as F

# Create random input logits and target labels
batch_size = 5
num_classes = 3
logits = torch.randn(batch_size, num_classes)
labels = torch.randint(0, num_classes, (batch_size,))

# Compute cross-entropy loss
loss = F.cross_entropy(logits, labels, weight=torch.tensor([0.5, 1.0, 1.5]), reduction='mean', label_smoothing=0.1)

print(f"Cross-Entropy Loss: {loss.item()}")