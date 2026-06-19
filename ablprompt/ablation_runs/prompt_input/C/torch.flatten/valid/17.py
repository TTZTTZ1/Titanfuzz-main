import torch

# Create a 4D tensor
tensor_4d = torch.randn(2, 3, 4, 5)

# Flatten the tensor from the second dimension to the fourth dimension
flattened_tensor = torch.flatten(tensor_4d, start_dim=1, end_dim=3)

print(flattened_tensor.shape)  # Output should be torch.Size([2, 60])