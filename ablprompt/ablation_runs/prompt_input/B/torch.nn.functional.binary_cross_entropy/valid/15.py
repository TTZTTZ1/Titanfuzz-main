import torch
import torch.nn.functional as F

# Generate random input and target tensors
batch_size = 32
num_classes = 5
input = torch.rand(batch_size, num_classes)
target = torch.randint(0, 2, (batch_size, num_classes)).float()

# Compute binary cross-entropy loss
loss = F.binary_cross_entropy(input, target)

print(f"Binary Cross-Entropy Loss: {loss.item()}")