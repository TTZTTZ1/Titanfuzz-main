import torch
import torch.nn.functional as F

# Example usage of binary_cross_entropy
input_tensor = torch.tensor([[0.1, 0.4, 0.3], [0.8, 0.2, 0.5]])
target_tensor = torch.tensor([[0, 1, 0], [1, 0, 1]])

# Compute binary cross-entropy loss
loss = F.binary_cross_entropy(input_tensor, target_tensor)

print(f"Binary Cross-Entropy Loss: {loss.item()}")