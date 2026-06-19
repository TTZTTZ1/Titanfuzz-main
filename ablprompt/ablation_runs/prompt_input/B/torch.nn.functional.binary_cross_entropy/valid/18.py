import torch
from torch.nn.functional import binary_cross_entropy

# Generate random input and target tensors
input_tensor = torch.rand(3, requires_grad=True)
target_tensor = torch.randint(0, 2, (3,), dtype=torch.float)

# Compute binary cross-entropy loss
loss = binary_cross_entropy(input_tensor, target_tensor, reduction='mean')

print(f"Input Tensor: {input_tensor}")
print(f"Target Tensor: {target_tensor}")
print(f"Loss: {loss.item()}")