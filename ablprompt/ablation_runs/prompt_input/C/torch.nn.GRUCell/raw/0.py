import torch

# Initialize the GRUCell
gru_cell = torch.nn.GRUCell(input_size=10, hidden_size=20)

# Input tensor (batch_size, input_size)
input_tensor = torch.randn(5, 10)

# Hidden state initialization (batch_size, hidden_size)
hidden_state = torch.zeros(5, 20)

# Process the input through the GRUCell
updated_hidden_state = gru_cell(input_tensor, hidden_state)

print(updated_hidden_state)