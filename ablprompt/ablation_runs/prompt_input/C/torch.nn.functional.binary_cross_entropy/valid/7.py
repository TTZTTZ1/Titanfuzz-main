import torch

# Example inputs
input_probs = torch.tensor([[0.9, 0.1], [0.3, 0.7]], requires_grad=True)
targets = torch.tensor([[1.0, 0.0], [0.0, 1.0]])

# Compute binary cross-entropy loss
loss = torch.nn.functional.binary_cross_entropy(input_probs, targets)

print(f"Computed Loss: {loss.item()}")