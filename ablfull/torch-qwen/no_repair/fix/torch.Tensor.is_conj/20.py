
import torch
input_tensor = torch.tensor([(1 + 1j), (2 + 2j)], dtype=torch.complex64)
result = input_tensor.is_conj()
print(result)
