with open("test.txt","r") as file1:
    read1=file1.readlines()
for i in range(1,len(read1),2):
    orfs=str(read1[i])
    orf1ab=orfs[265:21553]#positions of the nucleotides
    orf1a=orfs[265:13483]#positions of the nucleotides
    sugp=orfs[21562:25384]#positions of the nucleotides
    orf3a=orfs[25392:26220]#positions of the nucleotides
    envp=orfs[26244:26472]#positions of the nucleotides
    memgp=orfs[26522:27191]#positions of the nucleotides
    orf6=orfs[27201:27387]#positions of the nucleotides
    orf7a=orfs[27393:27759]#positions of the nucleotides
    orf7b=orfs[27755:27887]#positions of the nucleotides
    orf8=orfs[27893:28259]#positions of the nucleotides
    nucp=orfs[28273:29533]#positions of the nucleotides
    orf10=orfs[29557:29674]#positions of the nucleotides
    with open("testorf.txt","a") as file2:
        file2.write("\n>orf1ab\n")
        file2.write(orf1ab)
        file2.write("\n>orf1a\n")
        file2.write(orf1a)
        file2.write("\n>sgp\n")
        file2.write(sugp)
        file2.write("\n>orf3a\n")
        file2.write(orf3a)
        file2.write("\n>envp\n")
        file2.write(envp)
        file2.write("\n>mgp\n")
        file2.write(memgp)
        file2.write("\n>orf6\n")
        file2.write(orf6)
        file2.write("\n>orf7a\n")
        file2.write(orf7a)
        file2.write("\n>orf7b\n")
        file2.write(orf7b)
        file2.write("\n>orf8\n")
        file2.write(orf8)
        file2.write("\n>nucp\n")
        file2.write(nucp)
        file2.write("\n>orf10\n")
        file2.write(orf10)
