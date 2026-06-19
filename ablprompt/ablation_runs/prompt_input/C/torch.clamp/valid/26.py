import torch

# Create a sample tensor
input_tensor = torch.tensor([-1.5, 0.3, 2.7, -0.8])

# Define the clamp limits
min_value = -1.0
max_value = 2.0

# Apply clamp operation
clamped_tensor = torch.clamp(input_tensor, min=min_value, max=max_value)

print("Original Tensor:", input_tensor)
print("Clamped Tensor:", clamped_tensor)