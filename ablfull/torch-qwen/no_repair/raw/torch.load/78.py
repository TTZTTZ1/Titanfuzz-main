import torch

# Create dummy file-like object
from io import BytesIO
data = b"__torch_signature_version 2.0\n_0\nS'cpu'\np0\n."
f = BytesIO(data)

# Prepare valid input data
map_location = "cpu"

# Call the target API
result = torch.load(f, map_location=map_location)