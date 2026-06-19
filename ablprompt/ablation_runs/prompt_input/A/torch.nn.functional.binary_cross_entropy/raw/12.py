import torch
import torch.nn.functional as F

# Example usage of binary cross-entropy loss function
input = torch.tensor([0.1, 0.4, 0.35], requires_grad=True)
target = torch.tensor([0, 1, 0])

loss = F.binary_cross_entropy(input, target)
print(loss)

# Backward pass to compute gradients
loss.backward()
print(input.grad)