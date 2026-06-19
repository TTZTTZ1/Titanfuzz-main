import torch
abs_tensor = torch.tensor([1.0, 2.0], dtype=torch.float32)
angle_tensor = torch.tensor([0.0, 1.5708], dtype=torch.float32)
result = torch.polar(abs=abs_tensor, angle=angle_tensor)