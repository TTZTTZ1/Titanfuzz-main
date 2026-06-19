import torch
import io
sample_tensor = torch.tensor([1.0, 2.0, 3.0])
buffer = io.BytesIO()
torch.save(sample_tensor, buffer)
buffer.seek(0)
result = torch.load(buffer)
print(result)