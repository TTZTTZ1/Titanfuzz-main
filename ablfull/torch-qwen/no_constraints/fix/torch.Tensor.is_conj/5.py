import torch
input_tensor = torch.tensor([(1 + 1j), (2 + 2j)])
result = input_tensor.is_conj()
print(result)