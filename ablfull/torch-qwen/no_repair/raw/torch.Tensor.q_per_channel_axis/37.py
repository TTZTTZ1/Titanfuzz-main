import torch

# Generate input data
tensor = torch.randn(4, 3, 8, 8)
dtype = torch.quint8
factory_kwargs = {'device': 'cpu', 'dtype': dtype}

# Call the API
q_tensor = tensor.q_per_channel_axis(factory_kwargs=factory_kwargs)