
import torch
input_data = torch.tensor([(1 + 2j), (3 + 4j)], dtype=torch.complex64)
result = input_data.is_conj()
print(result)
