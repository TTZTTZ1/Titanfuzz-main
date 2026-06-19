import torch
import torch.nn.functional as F

# Create random input and target tensors
input = torch.randn(3, 5, requires_grad=True)
target = torch.tensor([1, 0, 4])

# Compute cross-entropy loss with class weights and label smoothing
weight = torch.tensor([0.1, 0.2, 0.3, 0.2, 0.2])
label_smoothing = 0.1

loss = F.cross_entropy(input, target, weight=weight, label_smoothing=label_smoothing)

print(loss)