import torch

# Generate random input and target tensors
input_probs = torch.rand((32, 64))
targets = torch.randint(0, 2, (32, 64)).float()

# Compute binary cross-entropy loss
loss = torch.nn.functional.binary_cross_entropy(input_probs, targets)

print(f"Computed Loss: {loss.item()}")