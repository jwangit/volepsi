#!/bin/sh
./out/build/linux/frontend/frontend -perf -test -w 4 -rate 0.8 -hybrid 1 -nn 12 -t 200000000 -ssize 1.28 > res0.log
mv res0.log* logs/nn12-ssize1283.csv
