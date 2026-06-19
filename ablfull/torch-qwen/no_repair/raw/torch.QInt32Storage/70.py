import torch

input_data = (torch.tensor([-128, -64, 0, 64, 127], dtype=torch.qint32),)
qint32_storage = torch.QInt32Storage(*input_data)