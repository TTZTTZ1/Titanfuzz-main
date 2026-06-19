import torch

# Define a simple model
class SimpleModel(torch.nn.Module):
    def __init__(self):
        super(SimpleModel, self).__init__()
        self.fc1 = torch.nn.Linear(10, 20)
        self.fc2 = torch.nn.Linear(20, 10)

model = SimpleModel()

# Create a sequential container of the model's layers
functions = [model.fc1, model.fc2]

# Prepare input data
input_data = torch.randn(1, 10)

# Call checkpoint_sequential
output = torch.utils.checkpoint.checkpoint_sequential(functions, segments=2, input=input_data, preserve_rng_state=True)