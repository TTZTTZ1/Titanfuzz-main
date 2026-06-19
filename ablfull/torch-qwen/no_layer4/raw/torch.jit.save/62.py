import torch

# Define a simple model
class SimpleModel(torch.nn.Module):
    def __init__(self):
        super(SimpleModel, self).__init__()
        self.linear = torch.nn.Linear(10, 1)

model = SimpleModel()

# Save the model to a file
torch.jit.save(model, 'simple_model.pt')