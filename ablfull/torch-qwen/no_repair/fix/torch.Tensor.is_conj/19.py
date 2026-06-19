
import torch
input_tensor = torch.tensor([[((- 1) + 0j)], [(2 + 0j)]], dtype=torch.complex64)
result = input_tensor.is_conj()
print(result)
