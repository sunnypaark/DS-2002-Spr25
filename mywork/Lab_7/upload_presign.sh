#!/bin/bash

FILE=$1
BUCKET=$2
EXPIRATION=$3

if [[ $# -ne 3 ]]; then
  echo "Usage: $0 <filename> <bucket> <expiration_seconds>"
  exit 1
fi

aws s3 cp "$FILE" s3://"$BUCKET"/
if [[ $? -ne 0 ]]; then
  echo "Upload failed."
  exit 1
fi

URL=$(aws s3 presign s3://"$BUCKET"/"$FILE" --expires-in "$EXPIRATION")
echo "Pre-signed URL (valid for $EXPIRATION seconds):"
echo "$URL"
