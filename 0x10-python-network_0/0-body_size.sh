#!/bin/bash
# Display the byte size of the HTTP response header for a given URL.

if [ $# -eq 0 ]; then
  echo "Usage: $0 URL"
  exit 1
fi

response=$(curl -s -w "%{size_download})" -o /dev/null $1)

echo $response
