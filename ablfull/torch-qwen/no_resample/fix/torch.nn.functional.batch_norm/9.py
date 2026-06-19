import torch
input_tensor = torch.randn(10, 3, 224, 224)
running_mean = torch.zeros(3)
running_var = torch.ones(3)
output_tensor = torch.nn.functional.batch_norm(input_tensor, running_mean, running_var)