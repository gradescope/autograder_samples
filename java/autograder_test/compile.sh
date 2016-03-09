#!/usr/bin/env bash

# Find all java files in src directory
java_files=$(find src -name "*.java")
javac -cp lib/*:. -d classes $java_files
