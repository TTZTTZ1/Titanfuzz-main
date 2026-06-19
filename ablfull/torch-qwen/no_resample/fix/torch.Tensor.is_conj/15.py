import torch
input_tensor = torch.tensor([(1 + 2j), (3 - 4j)])
result = input_tensor.is_conj()
print(result)