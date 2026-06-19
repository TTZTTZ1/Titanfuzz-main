import torch
input_tensor = torch.tensor([(1 + 0j), (2 + 0j)])
result = input_tensor.is_conj()
print(result)