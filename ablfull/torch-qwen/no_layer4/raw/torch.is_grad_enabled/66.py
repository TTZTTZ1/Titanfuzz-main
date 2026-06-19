import torch

# Disable gradient calculation for this context
with torch.no_grad():
    # Generate a dummy tensor
    dummy_tensor = torch.tensor([1.0, 2.0], requires_grad=False)
    
    # Call the API
    result = torch.is_grad_enabled()
    
print(result)