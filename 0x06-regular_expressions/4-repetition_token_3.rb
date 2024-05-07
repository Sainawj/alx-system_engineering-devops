#!/usr/bin/env ruby
# Check if there's exactly one argument provided
if ARGV.length == 1
  # Match "h", followed by zero or more occurrences of "b", then "t", and finally "n"
  matches = ARGV[0].scan(/hbt*n/)
  
  # Output all matches
  puts matches.join
else
  puts "Usage: #{$PROGRAM_NAME} <string>"
  exit 1
end
