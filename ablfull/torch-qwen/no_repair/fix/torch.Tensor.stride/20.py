
import torch
input_tensor = torch.randn(3)
stride_result = input_tensor.stride(None)
print(stride_result)
