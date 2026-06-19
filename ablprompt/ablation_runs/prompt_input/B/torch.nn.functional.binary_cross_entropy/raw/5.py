import torch
from torch.nn.functional import binary_cross_entropy

# Generate random input and target tensors
input_probs = torch.rand(3, 5)  # Predicted probabilities
target_labels = torch.randint(0, 2, (3, 5)).float()  # Target labels (binary)

# Compute binary cross-entropy loss
loss = binary_cross_entropy(input_probs, target_labels, reduction='mean')

print(f"Computed Loss: {loss.item()}")