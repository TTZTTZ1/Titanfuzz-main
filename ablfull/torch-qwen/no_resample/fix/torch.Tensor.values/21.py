import torch
tensor = torch.sparse_coo_tensor(indices=torch.tensor([[0, 1], [2, 3]]), values=torch.tensor([4.0, 5.0]), size=(4, 4))
tensor = tensor.coalesce()
values = tensor.values()
print(values)