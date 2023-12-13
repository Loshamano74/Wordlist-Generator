#!/bin/bash

# Directories to preserve
preserve_directories=("directory1" "directory2")  # Add the directories you want to preserve

# Check for changes in directories to preserve
for dir in "${preserve_directories[@]}"; do
  if [[ -d "$dir" ]]; then
    echo "Preserving directory: $dir"
    mv "$dir" /tmp  # Move the directory to a temporary location
  fi
done

# Fetch the latest changes from the remote repository
git fetch origin

# Reset the local branch to match the remote branch
git reset --hard origin/main  # Replace 'main' with your branch name if different

# Move back the preserved directories
for dir in "${preserve_directories[@]}"; do
  if [[ -d "/tmp/$dir" ]]; then
    echo "Restoring directory: $dir"
    mv "/tmp/$dir" .
  fi
done
