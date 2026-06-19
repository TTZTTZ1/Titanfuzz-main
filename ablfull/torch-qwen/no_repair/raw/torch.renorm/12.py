import torch

input_tensor = torch.randn(3, 4)
p_value = 2.0
dim_value = 1
maxnorm_value = 1.5

result = torch.renorm(input_tensor, p=p_value, dim=dim_value, maxnorm=maxnorm_value)