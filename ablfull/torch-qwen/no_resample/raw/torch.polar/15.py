import torch

# Prepare input data
abs_tensor = torch.tensor([1.0], dtype=torch.float32)
angle_tensor = torch.tensor([0.5], dtype=torch.float32)

# Call the API
result = torch.polar(abs=abs_tensor, angle=angle_tensor)