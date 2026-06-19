import torch

# Example usage of torch.clamp
tensor = torch.tensor([-1.0, 2.0, 3.0, -4.0])
clamped_tensor = torch.clamp(tensor, min=0, max=2)
print(clamped_tensor)  # Output: tensor([0., 2., 2., 0.])