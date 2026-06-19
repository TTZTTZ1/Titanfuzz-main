import torch
import torch.nn.functional as F

# Example input and target tensors
input_tensor = torch.tensor([0.1, 0.4, 0.35, 0.8], requires_grad=True)
target_tensor = torch.tensor([0, 0, 1, 1])

# Compute binary cross-entropy loss
loss = F.binary_cross_entropy(input_tensor, target_tensor, reduction='mean')

print(f"Computed Loss: {loss.item()}")