#!/usr/bin/env bash

b=$((22))
printf "\ec\e[1;1H\e[33m MR. MIKE EDWARDS\n"
for((a=3;a<=21;a++)); do
    b=$((b-1))
    printf "\e[34m\e[${a};3H×"
    printf "\e[36m\e[${a};${a}H×"
    printf "\e[34m\e[21;${a}H×"
    printf "\e[${a};21H×"
    printf "\e[3;${a}H×"
    printf "\e[12;${a}H×"
    printf "\e[31m\e[${a};12H×"
    printf "\e[36m\e[${b};${a}H×"
    printf "\e[100;1H"
    sleep 0.00000000000000000001
done
printf "\e[21;1H\n"
