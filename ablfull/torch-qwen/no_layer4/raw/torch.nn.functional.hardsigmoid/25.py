import torch

input_tensor = torch.tensor([-2.0, -1.0, 0.0, 1.0, 2.0], dtype=torch.float)
result = torch.nn.functional.hardsigmoid(input_tensor)