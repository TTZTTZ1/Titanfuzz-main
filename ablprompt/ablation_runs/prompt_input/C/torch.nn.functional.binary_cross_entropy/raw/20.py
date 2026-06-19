import torch
import torch.nn.functional as F

# Example usage of binary_cross_entropy
input_tensor = torch.tensor([0.1, 0.4, 0.35, 0.8], requires_grad=True)
target_tensor = torch.tensor([0, 0, 1, 1])
loss = F.binary_cross_entropy(input_tensor, target_tensor)

print(f"Loss: {loss.item()}")
loss.backward()
print(f"Gradients of input_tensor: {input_tensor.grad}")