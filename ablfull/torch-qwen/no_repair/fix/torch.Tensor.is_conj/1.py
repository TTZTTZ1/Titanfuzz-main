
import torch
input_tensor = torch.tensor([[(1 + 0j), (2 + 0j)], [(3 + 0j), (4 + 0j)]])
result = input_tensor.is_conj()
print(result)
