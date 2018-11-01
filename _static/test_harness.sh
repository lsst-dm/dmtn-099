#!/bin/bash

for i in {1..30}
do
  $1 & > /dev/null 2>1
done
