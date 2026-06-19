import torch
data = [0, 1, (- 1), 255, (- 256)]
storage = torch.QInt32Storage(data)