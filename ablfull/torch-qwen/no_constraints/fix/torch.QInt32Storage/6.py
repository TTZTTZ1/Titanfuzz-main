import torch
data = torch.randint((- 128), 128, (10,), dtype=torch.int8)
untyped_storage = data.untyped_storage()
storage = torch.QInt32Storage(wrap_storage=untyped_storage)