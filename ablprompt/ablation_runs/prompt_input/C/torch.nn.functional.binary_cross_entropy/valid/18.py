import torch
import torch.nn.functional as F

# Example tensors
input_tensor = torch.tensor([[0.3, 0.7], [0.8, 0.2]])
target_tensor = torch.tensor([[0.0, 1.0], [1.0, 0.0]])

# Compute binary cross-entropy loss
loss = F.binary_cross_entropy(input_tensor, target_tensor)

print("Binary Cross-Entropy Loss:", loss.item())