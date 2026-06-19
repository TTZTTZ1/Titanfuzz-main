import torch
from torch.nn.functional import binary_cross_entropy

# Example usage of binary_cross_entropy
input_probs = torch.tensor([0.9, 0.3, 0.7], requires_grad=True)
targets = torch.tensor([1.0, 0.0, 1.0])
weights = torch.tensor([0.5, 1.0, 0.8])

loss = binary_cross_entropy(input_probs, targets, weight=weights, reduction='mean')
print(loss)

# Backward pass to compute gradients
loss.backward()
print(input_probs.grad)