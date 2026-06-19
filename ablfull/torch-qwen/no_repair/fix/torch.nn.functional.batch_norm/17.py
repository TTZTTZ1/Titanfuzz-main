
import torch
(N, C, H, W) = (2, 3, 4, 5)
input_data = torch.randn(N, C, H, W, dtype=torch.float32)
running_mean = torch.zeros(C, dtype=torch.float32)
running_var = torch.ones(C, dtype=torch.float32)
output = torch.nn.functional.batch_norm(input_data, running_mean, running_var, training=True)
