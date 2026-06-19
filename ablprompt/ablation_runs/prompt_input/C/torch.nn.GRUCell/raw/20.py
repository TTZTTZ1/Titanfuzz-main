import torch

# Define the input size and hidden size
input_size = 10
hidden_size = 20

# Create an instance of GRUCell
gru_cell = torch.nn.GRUCell(input_size, hidden_size)

# Initialize input and hidden state
input_tensor = torch.randn(1, input_size)
hidden_state = torch.randn(1, hidden_size)

# Update the hidden state using GRUCell
updated_hidden_state = gru_cell(input_tensor, hidden_state)

print(updated_hidden_state)