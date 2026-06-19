import torch

abs_tensor = torch.tensor([1.0, 2.0], dtype=torch.float32)
angle_tensor = torch.tensor([0.5, 1.0], dtype=torch.float32)
out_tensor = torch.tensor([0j, 0j], dtype=torch.complex64)

result = torch.polar(abs=abs_tensor, angle=angle_tensor, out=out_tensor)