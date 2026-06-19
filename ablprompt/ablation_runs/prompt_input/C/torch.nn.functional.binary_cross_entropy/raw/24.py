import torch
import torch.nn.functional as F

# Example tensors
input_tensor = torch.tensor([0.1, 0.4, 0.35], requires_grad=True)
target_tensor = torch.tensor([0, 1, 0])

# Compute binary cross-entropy loss
loss = F.binary_cross_entropy(input_tensor, target_tensor)

print(f"Computed Loss: {loss.item()}")