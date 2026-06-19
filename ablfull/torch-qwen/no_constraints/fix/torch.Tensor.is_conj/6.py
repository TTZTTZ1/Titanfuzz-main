import torch
input_data = torch.tensor([[(1 + 1j), (2 + 2j)], [(3 + 3j), (4 + 4j)]])
result = input_data.is_conj()
print(result)