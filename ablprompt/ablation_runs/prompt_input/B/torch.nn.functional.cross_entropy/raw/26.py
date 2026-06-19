import torch
import torch.nn.functional as F

# Create random input and target tensors
batch_size = 5
num_classes = 3
input = torch.randn(batch_size, num_classes)
target = torch.randint(0, num_classes, (batch_size,))

# Compute cross-entropy loss
loss = F.cross_entropy(input, target, reduction='mean')
print(loss.item())