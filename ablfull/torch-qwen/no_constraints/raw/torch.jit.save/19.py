import torch

# Task 2: Generate input data
class MyModel(torch.nn.Module):
    def __init__(self):
        super(MyModel, self).__init__()
        self.fc = torch.nn.Linear(10, 5)

    def forward(self, x):
        return self.fc(x)

model = MyModel()
input_data = torch.randn(1, 10)
scripted_model = torch.jit.script(model)
f = "my_scripted_model.pt"

# Task 3: Call the API torch.jit.save
torch.jit.save(scripted_model, f)