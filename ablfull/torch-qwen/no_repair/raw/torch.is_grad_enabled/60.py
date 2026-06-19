import torch

# Set gradient calculation to True
x = torch.tensor(2.0, requires_grad=True)
y = x**2

# Enable or disable gradient calculation using torch.set_grad_enabled
enabled = torch.is_grad_enabled()
print(f"Gradient enabled: {enabled}")

# Temporarily disable gradient calculation
with torch.no_grad():
    z = x**2
    print(f"Gradient enabled within context manager: {torch.is_grad_enabled()}")