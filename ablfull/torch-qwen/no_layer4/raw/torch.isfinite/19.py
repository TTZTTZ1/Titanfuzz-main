import torch

# Generate a tensor with finite values to test torch.isfinite
input_tensor = torch.tensor([1.0, -1.0, 0.0], dtype=torch.float32)

# Call torch.isfinite
result = torch.isfinite(input_tensor)
print(result)