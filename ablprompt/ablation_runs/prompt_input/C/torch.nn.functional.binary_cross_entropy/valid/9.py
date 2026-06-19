import torch
import torch.nn.functional as F

# Example usage of binary_cross_entropy
input = torch.tensor([[0.3, 0.7], [0.8, 0.2]], requires_grad=True)
target = torch.tensor([[0.0, 1.0], [1.0, 0.0]])
weight = torch.tensor([0.5, 1.0])

loss = F.binary_cross_entropy(input, target, weight=weight, reduction='mean')
print(loss)
loss.backward()
print(input.grad)