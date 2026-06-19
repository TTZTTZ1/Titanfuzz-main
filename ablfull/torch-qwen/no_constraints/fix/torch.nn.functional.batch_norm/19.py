import torch
input_tensor = torch.randn(16, 3, 28, 28)
running_mean = torch.zeros(3)
running_var = torch.ones(3)
output_tensor = torch.nn.functional.batch_norm(input_tensor, running_mean, running_var, training=True)