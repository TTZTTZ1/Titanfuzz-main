import torch
input_tensor = torch.randn(4, 5)
p_value = 2.0
dim_value = 1
maxnorm_value = 1.0
result = torch.renorm(input_tensor, p=p_value, dim=dim_value, maxnorm=maxnorm_value)
print(result)