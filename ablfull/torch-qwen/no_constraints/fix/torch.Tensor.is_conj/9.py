import torch
input_tensor = torch.tensor([[((- 1) + 0j), (2 + 0j)], [(3 + 4j), ((- 5) + 6j)]])
result = input_tensor.is_conj()
print(result)