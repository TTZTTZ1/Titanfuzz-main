import torch

# Generate valid input data
data = [0, 127, 254]  # QUInt8Storage expects values between 0 and 254

# Call the API
storage = torch.QUInt8Storage(data=data)