
import torch
input_data = torch.tensor([(1 + 0j), (2 + 0j), (3 + 0j)])
result = input_data.is_conj()
print(result)
