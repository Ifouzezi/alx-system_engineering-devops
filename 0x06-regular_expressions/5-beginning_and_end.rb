#!/usr/bin/env ruby

pattern = /^h.n$/
puts ARGV[0].scan(pattern).join
