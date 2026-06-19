import torch
import torch.nn.functional as F

# Create random input tensor with shape (batch_size, num_classes)
batch_size = 5
num_classes = 3
input_tensor = torch.randn(batch_size, num_classes)

# Create target tensor with shape (batch_size)
target_tensor = torch.randint(0, num_classes, (batch_size,))

# Compute cross-entropy loss
loss = F.cross_entropy(input_tensor, target_tensor)

print(f"Cross-Entropy Loss: {loss.item()}")