
import torch
tensor = torch.tensor([[(1 + 0j), (2 + 0j)], [(3 + 0j), (4 + 0j)]])
result = tensor.is_conj()
print(result)
