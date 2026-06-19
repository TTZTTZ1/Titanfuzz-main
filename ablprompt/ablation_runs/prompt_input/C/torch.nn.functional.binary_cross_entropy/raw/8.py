import torch
import torch.nn.functional as F

# Example usage of torch.nn.functional.binary_cross_entropy
input_tensor = torch.tensor([0.3, 0.7, 0.2], requires_grad=True)
target_tensor = torch.tensor([0.0, 1.0, 0.0])
loss = F.binary_cross_entropy(input_tensor, target_tensor)
print(loss)
loss.backward()