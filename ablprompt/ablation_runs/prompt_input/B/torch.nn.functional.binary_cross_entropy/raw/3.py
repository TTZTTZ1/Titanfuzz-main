import torch
from torch.nn.functional import binary_cross_entropy

# Example usage of binary_cross_entropy
input_tensor = torch.tensor([0.3, 0.7, 0.2], requires_grad=True)
target_tensor = torch.tensor([0.0, 1.0, 0.0])
weight_tensor = torch.tensor([1.0, 2.0, 1.0])

loss = binary_cross_entropy(input_tensor, target_tensor, weight=weight_tensor, reduction='mean')
print(loss)

# Backward pass
loss.backward()
print(input_tensor.grad)