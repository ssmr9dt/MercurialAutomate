#!/bin/bash

if [ -z "$1" ];
then
        echo "error: Please set repository name"
        exit 1
fi

pushd /mnt/repo

if [ -d "$1" ];
then
  echo "error: Directory exists."
  exit 1
fi

hg init $1
chown www-data -R $1

pushd /mnt/asdf

ln -s ../repo/$1 $1

popd

popd

echo "success"
