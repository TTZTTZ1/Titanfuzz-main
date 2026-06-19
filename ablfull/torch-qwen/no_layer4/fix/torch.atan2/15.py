import torch
input_tensor = torch.tensor([[0.5, (- 0.5)], [1.0, (- 1.0)]], dtype=torch.float32)
other_tensor = torch.tensor([[(- 0.5), 0.5], [(- 1.0), 1.0]], dtype=torch.float32)
result = torch.atan2(input_tensor, other_tensor)