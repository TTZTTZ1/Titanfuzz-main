import torch

# Example usage of torch.nn.functional.binary_cross_entropy
input_probs = torch.tensor([0.9, 0.3, 0.7], requires_grad=True)
targets = torch.tensor([1.0, 0.0, 1.0])
weights = torch.tensor([1.0, 2.0, 1.0])

loss = torch.nn.functional.binary_cross_entropy(input_probs, targets, weight=weights, reduction='mean')
print(loss)

# Backward pass to compute gradients
loss.backward()
print(input_probs.grad)