#!/bin/bash
# Get the response body for a given URL for 200 status code responses.

response_file=$(mktemp)
response=$(curl -s -w "%{http_code}" -o "$response_file" "$1")
status_code=$(echo "$response" | awk '{print $2}')
if [ "$status_code" = "200" ]; then
  response_body=$(cat "$response_file")
  echo "$response_body"
fi

rm "$response_file"
