import torch

# Prepare valid input data
data = [0, -128, 127]  # Example QInt32 values within the range [-128, 127]

# Call the API
storage = torch.QInt32Storage(data=data)