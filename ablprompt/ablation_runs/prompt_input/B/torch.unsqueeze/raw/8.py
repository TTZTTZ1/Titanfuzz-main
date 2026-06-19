import torch

# Create a random tensor
input_tensor = torch.randn(3, 4)

# Unsqueeze at dimension 0
unsqueezed_tensor_0 = torch.unsqueeze(input_tensor, 0)
print("Unsqueezed at dim 0:", unsqueezed_tensor_0.shape)

# Unsqueeze at dimension -1
unsqueezed_tensor_neg1 = torch.unsqueeze(input_tensor, -1)
print("Unsqueezed at dim -1:", unsqueezed_tensor_neg1.shape)