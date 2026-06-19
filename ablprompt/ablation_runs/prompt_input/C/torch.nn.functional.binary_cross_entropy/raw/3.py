import torch

# Example tensors
input_tensor = torch.tensor([0.1, 0.4, 0.35, 0.8], requires_grad=True)
target_tensor = torch.tensor([0, 0, 1, 1])

# Compute binary cross-entropy loss
loss = torch.nn.functional.binary_cross_entropy(input_tensor, target_tensor)

print(f"Computed Loss: {loss.item()}")