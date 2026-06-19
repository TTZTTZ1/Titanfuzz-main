import torch
import torch.nn.functional as F

# Example usage of binary_cross_entropy
input_probs = torch.tensor([0.9, 0.1, 0.8], requires_grad=True)
targets = torch.tensor([1.0, 0.0, 1.0])
weights = torch.tensor([1.0, 2.0, 1.0])

loss = F.binary_cross_entropy(input_probs, targets, weight=weights, reduction='mean')
print(loss)

# Backward pass
loss.backward()
print(input_probs.grad)