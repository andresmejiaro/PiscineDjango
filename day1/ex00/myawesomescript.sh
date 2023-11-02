#!/bin/bash
(curl   -i -s  $1) | grep "Location:" | cut -d " " -f 2 2>/dev/null

