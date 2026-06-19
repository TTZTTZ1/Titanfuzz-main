import torch
input_data = torch.randint(0, 2, (5,))
result = input_data.bernoulli_()
print(result)