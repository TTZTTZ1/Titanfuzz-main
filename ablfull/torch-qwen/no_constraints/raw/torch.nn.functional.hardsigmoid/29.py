import torch

input_tensor = torch.tensor([-1.0, 0.0, 1.0], dtype=torch.float32)
result = torch.nn.functional.hardsigmoid(input_tensor)
print(result)