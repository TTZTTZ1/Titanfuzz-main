import torch
input_data = torch.tensor([(1 + 0j), (0 + 1j)])
result = input_data.is_conj()
print(result)