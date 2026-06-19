import torch

# Initialize the GRUCell
input_size = 10
hidden_size = 20
gru_cell = torch.nn.GRUCell(input_size, hidden_size)

# Create random input and hidden state
input_data = torch.randn(1, input_size)
hidden_state = torch.randn(1, hidden_size)

# Perform a forward pass through the GRUCell
new_hidden_state = gru_cell(input_data, hidden_state)

print(new_hidden_state)