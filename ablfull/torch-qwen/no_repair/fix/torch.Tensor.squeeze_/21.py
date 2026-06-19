
import torch
input_tensor = torch.randn(1, 1, 5)
input_tensor.squeeze_()
print(input_tensor)
