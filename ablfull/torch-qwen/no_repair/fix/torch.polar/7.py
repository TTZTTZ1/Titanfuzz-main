
import torch
abs_tensor = torch.tensor([1.0, 2.0], dtype=torch.float32)
angle_tensor = torch.tensor([0.0, 1.0], dtype=torch.float32)
result = torch.polar(abs_tensor, angle_tensor)
