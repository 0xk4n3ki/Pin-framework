#!/usr/bin/env python3

import subprocess

command = ["../../../pin", "-t", "obj-intel64/inscount0.so", "-o", "insCount.txt", "--", "./e7bc5d2c0cf4480348f5504196561297"]
charSet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789@-_."

def readInst():
    f = open("insCount.txt", "r")
    inst = f.read()
    inst = int(inst[6:-1])
    return inst

def argNum():
    instArr = []
    for i in range(4):
        print("[!] Arguments passed : ", i+1)
        args = "A "
        command.append(args)

        subprocess.run(command)

        inst = readInst()
        instArr.append(inst)
        print("[!]Instruction Count : ", inst)
    maxIndex = instArr.index(max(instArr))
    print("[+] number of arguments required by the binary : ", maxIndex+1)
    return maxIndex

def arglen():
    instArr = []
    for i in range(20):
        command = ["../../../pin", "-t", "obj-intel64/inscount0.so", "-o", "insCount.txt", "--", "./e7bc5d2c0cf4480348f5504196561297"]
        arg1 = "1"*(i+1)
        arg2 = "2"*10
        command.append(arg1)
        command.append(arg2)

        subprocess.run(command)

        inst = readInst()
        instArr.append(inst)
        print("[!] arg1 len passed : ", i+1, ", inst count : ", inst)
    maxIndex = instArr.index(max(instArr))
    print("[+] length of argument 1 should be : ", maxIndex+1)
    return maxIndex

def solveArg2(length):
    arg2 = "2"*(length)
    arg1 = "4815162342"
    for i in range(length):
        print("[!] i : ", i)
        instArr = []
        for j in charSet:
            arg2_list = list(arg2)
            arg2_list[i] = j
            arg2 = ''.join(arg2_list)
            command = ["../../../pin", "-t", "obj-intel64/inscount0.so", "-o", "insCount.txt", "--", "./e7bc5d2c0cf4480348f5504196561297"]
            command.append(arg1)
            command.append(arg2)

            subprocess.run(command)

            inst = readInst()
            instArr.append(inst)
            print("[!] char : ", j, "instruction count : ", inst)
        maxIndex = instArr.index(max(instArr))
        arg2_list = list(arg2)
        arg2_list[i] = charSet[maxIndex]
        arg2 = ''.join(arg2_list)
        print(arg2)

def solveArg1():
    arg2 = "a"*4
    arg1 = "1"*10
    for i in range(10):
        print("[!] i : ", i)
        instArr = []
        for j in charSet:
            arg1_list = list(arg1)
            arg1_list[i] = j
            arg1 = ''.join(arg1_list)
            command = ["../../../pin", "-t", "obj-intel64/inscount0.so", "-o", "insCount.txt", "--", "./e7bc5d2c0cf4480348f5504196561297"]
            command.append(arg1)
            command.append(arg2)

            subprocess.run(command)
            
            inst = readInst()
            instArr.append(inst)
            print("[!] char : ", j, "instruction count : ", inst)
        maxIndex = instArr.index(max(instArr))
        arg1_list = list(arg1)
        arg1_list[i] = charSet[maxIndex]
        arg1 = ''.join(arg1_list)
        print(instArr)

        

def main():
    # number_of_arguments = argNum()
    # arg1len = arglen()
    # solveArg1()
    solveArg2(50)

if __name__ == '__main__':
    main()
