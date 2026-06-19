import torch
from torch.nn.functional import binary_cross_entropy

# Example inputs
input_probs = torch.tensor([[0.9, 0.2], [0.3, 0.8]], requires_grad=True)
targets = torch.tensor([[1.0, 0.0], [0.0, 1.0]])

# Compute binary cross-entropy loss
loss = binary_cross_entropy(input_probs, targets, reduction='mean')

# Print the loss
print(f"Binary Cross-Entropy Loss: {loss.item()}")

# Backward pass to compute gradients
loss.backward()
print("Gradients of input_probs:", input_probs.grad)