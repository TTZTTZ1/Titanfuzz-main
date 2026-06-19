import torch
from io import BytesIO
dummy_tensor = torch.tensor([1.0, 2.0, 3.0])
buffer = BytesIO()
torch.save(dummy_tensor, buffer)
buffer.seek(0)
result = torch.load(buffer)