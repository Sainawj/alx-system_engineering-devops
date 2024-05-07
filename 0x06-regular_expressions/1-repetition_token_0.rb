#!/usr/bin/env ruby
# Check if there's exactly one argument provided
if ARGV.length == 1
  # Match "hbt" followed by 2 to 5 occurrences of "t" and then "n"
  matches = ARGV[0].scan(/hbt{2,5}n/)
  
  # Output all matches
  puts matches.join
else
  puts "Usage: #{$PROGRAM_NAME} <string>"
  exit 1
end
