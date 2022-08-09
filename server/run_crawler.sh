#!/bin/bash
for i in {1..200}
do
    python wiki_crawler.py
    echo "the $i th time that we executed script"
done