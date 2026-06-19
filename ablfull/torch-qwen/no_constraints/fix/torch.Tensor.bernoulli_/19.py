import torch
input_tensor = torch.tensor([[0.5, 0.7], [0.3, 0.9]])
result_tensor = input_tensor.bernoulli_()
print(result_tensor)