import torch
import torch.nn.functional as F

# Create a random input tensor with shape (batch_size, num_classes)
batch_size = 5
num_classes = 3
input_tensor = torch.randn(batch_size, num_classes)

# Create a random target tensor with shape (batch_size)
target_tensor = torch.randint(0, num_classes, (batch_size,))

# Define class weights
class_weights = torch.tensor([0.5, 1.0, 2.0])

# Compute cross-entropy loss
loss = F.cross_entropy(input_tensor, target_tensor, weight=class_weights, reduction='mean')

print(f"Cross-Entropy Loss: {loss.item()}")