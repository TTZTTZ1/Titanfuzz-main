import torch

data = [1, 2, 3]
storage = torch.tensor(data, dtype=torch.uint8).storage()
qint8_storage = torch.QUInt8Storage(wrap_storage=storage, dtype=torch.quint8, device='cpu')