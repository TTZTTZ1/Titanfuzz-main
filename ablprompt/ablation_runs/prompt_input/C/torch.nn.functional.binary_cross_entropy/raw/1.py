import torch

# Generate random predictions and targets
input_probs = torch.rand(10, requires_grad=True)
targets = torch.randint(0, 2, (10,), dtype=torch.float32)

# Compute binary cross-entropy loss
loss = torch.nn.functional.binary_cross_entropy(input_probs, targets)

print(f"Computed Loss: {loss.item()}")