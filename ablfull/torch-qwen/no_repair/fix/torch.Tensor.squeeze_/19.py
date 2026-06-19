
import torch
input_tensor = torch.randn(1, 1, 3)
input_tensor.squeeze_()
print(input_tensor)
