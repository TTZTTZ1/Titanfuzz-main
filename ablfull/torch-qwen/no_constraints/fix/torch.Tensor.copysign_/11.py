import torch
input_tensor = torch.tensor([(- 1.0), 2.0, (- 3.0)])
sign_tensor = torch.tensor([1.0, (- 1.0), 1.0])
input_tensor.copysign_(sign_tensor)
print(input_tensor)