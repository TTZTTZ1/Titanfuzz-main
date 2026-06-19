import torch
shape = (3, 4)
dtype = torch.int64
tensor = torch.empty(shape, dtype=dtype).random_(0, 10)
print(tensor)