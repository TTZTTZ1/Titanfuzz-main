import torch
input_tensor = torch.tensor([[(1 + 0j), (2 + 3j)], [(4 + 5j), (6 - 7j)]])
result = input_tensor.is_conj()
print(result)