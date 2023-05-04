#!/usr/bin/env ruby

pattern = /hbt+n/
puts ARGV[0].scan(pattern).join
