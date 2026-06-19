import torch

# Prepare valid input data
input_data = (torch.randint(0, 256, (4,)),)

# Call the API
result = torch.QInt32Storage(*input_data)