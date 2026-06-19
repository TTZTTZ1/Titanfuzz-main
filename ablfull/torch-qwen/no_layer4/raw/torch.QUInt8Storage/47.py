import torch

# Prepare valid input data
data = [0, 1, 2, 3, 4]  # Example sequence data

# Call the API with prepared data
storage = torch.QUInt8Storage(data=data)