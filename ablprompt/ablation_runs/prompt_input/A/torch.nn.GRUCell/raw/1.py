import torch

# Initialize input and hidden state
input_size = 10
hidden_size = 20
batch_size = 3

# Create an instance of GRUCell
gru_cell = torch.nn.GRUCell(input_size, hidden_size)

# Randomly initialize input and hidden state
input_data = torch.randn(batch_size, input_size)
hidden_state = torch.randn(batch_size, hidden_size)

# Perform a forward pass through the GRUCell
new_hidden_state = gru_cell(input_data, hidden_state)

print(new_hidden_state)