import torch
input_tensor = torch.randn(3, 4)
raveled_tensor = input_tensor.ravel()
print(raveled_tensor)