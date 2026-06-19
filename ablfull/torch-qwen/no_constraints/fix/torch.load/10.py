import torch
import io
dummy_tensor = torch.randn(3, 3)
buffer = io.BytesIO()
torch.save(dummy_tensor, buffer)
buffer.seek(0)
result = torch.load(buffer)