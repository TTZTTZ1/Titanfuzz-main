import torch

# Prepare a simple PyTorch script module
class MyModel(torch.nn.Module):
    def __init__(self):
        super(MyModel, self).__init__()
        self.linear = torch.nn.Linear(10, 1)

    def forward(self, x):
        return self.linear(x)

model = MyModel()

# Define the output file path
file_path = 'model.pt'

# Call torch.jit.save to save the model
torch.jit.save(model, file_path)