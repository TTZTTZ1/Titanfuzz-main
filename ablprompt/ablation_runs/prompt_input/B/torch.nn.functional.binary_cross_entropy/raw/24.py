import torch
from torch.nn.functional import binary_cross_entropy

# Example usage of binary_cross_entropy
input = torch.tensor([0.1, 0.4, 0.35], requires_grad=True)
target = torch.tensor([0, 1, 0])
weight = torch.tensor([1.0, 2.0, 1.0])

loss = binary_cross_entropy(input, target, weight=weight, reduction='mean')
print(loss)
loss.backward()