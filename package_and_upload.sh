#!/bin/bash

set -e

env="dev"
upload="false"

while [ $# -gt 0 ]; do
  case "$1" in
    --upload=*)
      upload="${1#*=}"
      ;;
    --env=*)
      env="${1#*=}"
      ;;
    *)
      printf "***************************\n"
      printf "* Error: Invalid argument.*\n"
      printf "***************************\n"
      exit 1
  esac
  shift
done

rm -rf dist/
python3 setup.py sdist bdist_wheel

if [ $env == "dev" ] && [ $upload == "true" ]; then
  twine upload --repository testpypi dist/*
  exit
fi

if [ $env == "prod" ] && [ $upload == "true" ]; then
  twine upload --repository dist/*
  exit
fi
