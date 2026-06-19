import torch
import torch.nn.functional as F

# Example usage of binary_cross_entropy
input_tensor = torch.tensor([0.5, 0.3, 0.7], requires_grad=True)
target_tensor = torch.tensor([1.0, 0.0, 1.0])
loss = F.binary_cross_entropy(input_tensor, target_tensor)

print("Input Tensor:", input_tensor)
print("Target Tensor:", target_tensor)
print("Loss:", loss)