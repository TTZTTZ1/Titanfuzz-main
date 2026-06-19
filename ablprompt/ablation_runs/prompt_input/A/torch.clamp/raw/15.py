import torch

# Example usage of torch.clamp
tensor = torch.tensor([-1.0, 0.0, 1.0, 2.0])
clamped_tensor = torch.clamp(tensor, min=0, max=1)
print(clamped_tensor)  # Output: tensor([0., 0., 1., 1.])