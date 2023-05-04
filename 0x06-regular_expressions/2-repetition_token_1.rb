#!/usr/bin/env ruby

pattern = /\(\d{3}\)\s\d{3}-\d{4}/
puts ARGV[0].scan(pattern).join
