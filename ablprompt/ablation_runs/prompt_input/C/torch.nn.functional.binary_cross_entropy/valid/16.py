import torch
import torch.nn.functional as F

# Example usage of binary_cross_entropy
input_probs = torch.tensor([0.8, 0.3, 0.7], requires_grad=True)
targets = torch.tensor([1.0, 0.0, 1.0])
loss = F.binary_cross_entropy(input_probs, targets)

print(f"Loss: {loss.item()}")
loss.backward()
print(f"Gradients of input_probs: {input_probs.grad}")