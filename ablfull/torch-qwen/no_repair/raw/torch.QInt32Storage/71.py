import torch

# Prepare valid input data
input_data = (1, 2, 3)

# Call the API with the prepared input data
storage = torch.QInt32Storage(*input_data)