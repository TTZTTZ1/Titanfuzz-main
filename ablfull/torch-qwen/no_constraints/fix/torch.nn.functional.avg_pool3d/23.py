import torch
input_tensor = torch.randn(1, 3, 4, 4, 4)
output = torch.nn.functional.avg_pool3d(input_tensor, kernel_size=(2, 2, 2))
print(output)