import torch
import torch.nn.functional as F

# Example usage of binary_cross_entropy
input = torch.tensor([0.5, 0.3, 0.2], requires_grad=True)
target = torch.tensor([1.0, 0.0, 1.0])

loss = F.binary_cross_entropy(input, target)
print(loss)

# Backward pass to compute gradients
loss.backward()
print(input.grad)