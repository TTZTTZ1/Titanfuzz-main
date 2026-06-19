import torch

data = [1, 2, 3]
storage = torch.tensor(data).cpu().detach()
quint8_storage = torch.QUInt8Storage(storage=storage, dtype=torch.quint8)