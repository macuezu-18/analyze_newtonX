#!/bin/bash

for x in *.json; do bagel "${x%.json}" ; done
