import torch
import torch.nn.functional as F

# Example usage of binary_cross_entropy
input_tensor = torch.tensor([0.5, 0.8, 0.3], requires_grad=True)
target_tensor = torch.tensor([0.0, 1.0, 0.0])

# Compute binary cross-entropy loss
loss = F.binary_cross_entropy(input_tensor, target_tensor)

print(f"Computed Loss: {loss.item()}")