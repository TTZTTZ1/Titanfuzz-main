import torch
import torch.nn.functional as F

# Example usage of binary cross-entropy loss
input = torch.tensor([0.5, 0.3, 0.7], requires_grad=True)
target = torch.tensor([1.0, 0.0, 1.0])

loss = F.binary_cross_entropy(input, target)

print("Loss:", loss.item())
loss.backward()
print("Gradients:", input.grad)