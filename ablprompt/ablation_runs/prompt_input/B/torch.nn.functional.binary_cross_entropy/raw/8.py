import torch
import torch.nn.functional as F

# Generate random predictions and targets
batch_size = 32
num_classes = 5
input = torch.rand(batch_size, num_classes)
target = torch.randint(0, 2, (batch_size, num_classes)).float()

# Apply sigmoid activation to input
input_sigmoid = torch.sigmoid(input)

# Compute binary cross-entropy loss
loss = F.binary_cross_entropy(input_sigmoid, target, reduction='mean')

print(f"Computed Loss: {loss.item()}")