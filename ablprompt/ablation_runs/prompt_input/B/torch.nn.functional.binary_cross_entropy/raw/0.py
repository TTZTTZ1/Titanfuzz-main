import torch
import torch.nn.functional as F

# Example inputs
input_probs = torch.tensor([[0.1, 0.4, 0.3], [0.8, 0.2, 0.5]], requires_grad=True)
targets = torch.tensor([[0.0, 1.0, 0.0], [1.0, 0.0, 1.0]])

# Compute binary cross-entropy loss
loss = F.binary_cross_entropy(input_probs, targets)

print(f"Loss: {loss.item()}")
loss.backward()
print("Gradients:", input_probs.grad)