import torch
import torch.nn.functional as F

# Example inputs
input = torch.tensor([[0.1, 0.4, 0.3], [0.8, 0.2, 0.5]], requires_grad=True)
target = torch.tensor([[0, 1, 0], [1, 0, 1]])

# Compute binary cross-entropy loss
loss = F.binary_cross_entropy(input, target)

print("Loss:", loss.item())
loss.backward()
print("Gradients:", input.grad)