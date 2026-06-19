import torch
input_tensor = torch.randn(2, 3)
raveled_tensor = input_tensor.ravel()
print(raveled_tensor)