
import torch
input_tensors = [torch.randn(3), torch.randn(4)]
params_list = torch.nn.ParameterList(input_tensors)
