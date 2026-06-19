import torch

# Enable gradient calculation
torch.set_grad_enabled(True)

# Prepare input data (e.g., a tensor)
input_tensor = torch.tensor([1.0, 2.0], requires_grad=True)

# Call the API
result = torch.is_grad_enabled()

print(result)