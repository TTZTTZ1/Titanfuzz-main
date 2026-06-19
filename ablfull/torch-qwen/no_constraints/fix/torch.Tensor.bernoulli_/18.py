import torch
input_tensor = torch.tensor([0.5], requires_grad=False)
result_tensor = input_tensor.bernoulli_()