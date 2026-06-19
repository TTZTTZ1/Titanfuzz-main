import torch
import torch.nn.functional as F

# Generate random input and target tensors
input_tensor = torch.rand(3, 4)  # Random predictions
target_tensor = torch.randint(0, 2, (3, 4)).float()  # Binary targets

# Compute binary cross-entropy loss
loss = F.binary_cross_entropy(input_tensor, target_tensor)

print(f"Computed Loss: {loss.item()}")