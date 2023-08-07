#!/bin/sh
./out/build/linux/frontend/frontend -perf -test -hybrid 0 -nn 16  -w 5 -ssize 1.221 -b 32 -t 100000 >> res.log
mv res.log* paxoslog/nn16-ssize1221.csv
./out/build/linux/frontend/frontend -perf -test -hybrid 0 -nn 16  -w 5 -ssize 1.222 -b 32 -t 100000 >> res.log
mv res.log* paxoslog/nn16-ssize1222.csv
