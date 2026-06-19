import torch

# Define the input size, hidden size, and number of time steps
input_size = 10
hidden_size = 20
num_steps = 5

# Create a random input tensor and initial hidden state
input_tensor = torch.randn(num_steps, 1, input_size)
initial_hidden_state = torch.randn(1, 1, hidden_size)

# Initialize the GRUCell
gru_cell = torch.nn.GRUCell(input_size, hidden_size)

# Process the input sequence through the GRUCell
hidden_states = []
for i in range(num_steps):
    current_input = input_tensor[i]
    current_hidden_state = gru_cell(current_input, initial_hidden_state)
    hidden_states.append(current_hidden_state)
    initial_hidden_state = current_hidden_state

# Convert list of hidden states to a tensor
final_hidden_states = torch.stack(hidden_states)

print(final_hidden_states)