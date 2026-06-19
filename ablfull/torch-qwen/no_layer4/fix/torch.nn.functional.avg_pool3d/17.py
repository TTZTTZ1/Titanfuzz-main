import torch
input_tensor = torch.randn(1, 1, 5, 5, 5)
avg_pooled_output = torch.nn.functional.avg_pool3d(input=input_tensor, kernel_size=3, stride=1, padding=1, ceil_mode=False, count_include_pad=True)