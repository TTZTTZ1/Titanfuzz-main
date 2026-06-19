import torch
input_data = torch.tensor([(1 + 1j), (2 + 2j)])
result = input_data.is_conj()
print(result)