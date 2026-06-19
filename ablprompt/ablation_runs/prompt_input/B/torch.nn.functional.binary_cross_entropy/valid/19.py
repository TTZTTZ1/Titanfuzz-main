import torch
import torch.nn.functional as F

# Create random input and target tensors
batch_size = 32
input = torch.rand(batch_size, requires_grad=True)
target = torch.randint(0, 2, (batch_size,), dtype=torch.float)

# Compute binary cross-entropy loss
loss = F.binary_cross_entropy(input, target, reduction='mean')

# Print the loss
print(f"Binary Cross-Entropy Loss: {loss.item()}")

# Backward pass to compute gradients
loss.backward()