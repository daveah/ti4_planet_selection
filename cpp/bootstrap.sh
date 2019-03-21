#!/usr/bin/env bash

mkdir release
cd release
cmake -DCMAKE_BUILD_TYPE=Release ..
cd ..
mkdir debug
cd debug
cmake -DCMAKE_BUILD_TYPE=Debug ..
cd ..
mkdir rel_with_debug
cd rel_with_debug
cmake -DCMAKE_BUILD_TYPE=RelWithDebInfo ..

