import torch

# Example usage of torch.clamp
tensor = torch.tensor([-1.0, 2.5, -3.2, 4.8])
clamped_tensor = torch.clamp(tensor, min=-2.0, max=3.0)
print(clamped_tensor)