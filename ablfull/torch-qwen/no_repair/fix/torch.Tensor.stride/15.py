
import torch
tensor = torch.tensor([[1.0, 2.0], [3.0, 4.0]])
stride = tensor.stride(None)
print(stride)
