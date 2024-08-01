#!/usr/bin/env ruby

require './drand48'

(0..1000000).each do |n|
  srand48(n)
  puts drand48
end
