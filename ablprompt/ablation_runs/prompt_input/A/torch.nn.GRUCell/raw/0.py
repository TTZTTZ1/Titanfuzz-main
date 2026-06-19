import torch

# Initialize GRUCell
input_size = 10
hidden_size = 20
gru_cell = torch.nn.GRUCell(input_size, hidden_size)

# Input data and hidden state
input_data = torch.randn(5, input_size)  # Sequence of 5 inputs, each of size 10
hidden_state = torch.randn(hidden_size)   # Initial hidden state of size 20

# Forward pass through GRUCell
new_hidden_state = gru_cell(input_data, hidden_state)
print(new_hidden_state)