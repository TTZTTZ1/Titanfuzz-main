import torch
import torch.nn.functional as F

# Create some random logits and targets
logits = torch.randn(5, 3)
targets = torch.randint(0, 3, (5,))

# Compute cross-entropy loss with class weights and label smoothing
class_weights = torch.tensor([0.5, 1.0, 1.5])
label_smoothing = 0.1

loss = F.cross_entropy(logits, targets, weight=class_weights, label_smoothing=label_smoothing)

print(loss)