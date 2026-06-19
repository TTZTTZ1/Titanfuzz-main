import torch
import torch.nn.functional as F

# Example inputs
input_probs = torch.tensor([0.9, 0.1, 0.8], requires_grad=True)
targets = torch.tensor([1.0, 0.0, 1.0])

# Compute binary cross-entropy loss
loss = F.binary_cross_entropy(input_probs, targets)

# Print the loss
print("Binary Cross-Entropy Loss:", loss.item())

# Backward pass to compute gradients
loss.backward()
print("Gradients of input_probs:", input_probs.grad)