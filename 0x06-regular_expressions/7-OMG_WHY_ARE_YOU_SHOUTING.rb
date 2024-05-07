#!/usr/bin/env ruby
# Function to find all occurrences of uppercase letters in the input string
def find_uppercase(input)
  input.scan(/[A-Z]+/)
end

# Extract the first argument from the command-line arguments
input_string = ARGV[0]

# Call the function to find occurrences and join them
puts find_uppercase(input_string).join
