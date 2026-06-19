
import torch
input_tensor = torch.tensor([(- 1.5), 0.0, 1.5], dtype=torch.float32)
output_tensor = torch.fix(input_tensor)
