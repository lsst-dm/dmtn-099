#!/bin/bash

for i in {1..50}
do
  $1 & > /dev/null 2>1
done
