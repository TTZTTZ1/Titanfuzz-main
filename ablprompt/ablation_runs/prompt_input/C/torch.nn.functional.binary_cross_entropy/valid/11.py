import torch
import torch.nn.functional as F

# Example input and target tensors
input_tensor = torch.tensor([0.5, 0.3, 0.8], requires_grad=True)
target_tensor = torch.tensor([1.0, 0.0, 1.0])

# Compute binary cross-entropy loss
loss = F.binary_cross_entropy(input_tensor, target_tensor)

print(f"Computed Loss: {loss.item()}")