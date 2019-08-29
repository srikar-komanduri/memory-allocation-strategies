# memory allocation strategy with fixed partition method

def first_fit(files,mem):
        print("**********FIRST FIT**********")
        print("FILES SIZES","              ","BLOCK-NO","              ","IF")
        no_of_blocks=len(mem)
        no_of_files=len(files)
        flag_m=[0]* no_of_blocks                # 0 is for available
        flag_f=[0]* no_of_files                 # 0 is for not allocated 
        TIF=0
        for i in range(no_of_files):
                IF=0
                for j in range(no_of_blocks):
                        if flag_m[j]==0 and mem[j]>=files[i] and files[i]>0:
                                flag_m[j]=1
                                flag_f[i]=1
                                IF+=mem[j]-files[i]
                                TIF+=IF
                                print(files[i],"                              ",j+1,"                              ",IF)
                                files[i]=0
        print("total Internal fragmentation produced is: ",TIF,"\n\n")

        for i in range(no_of_files):
                if flag_f[i]==0:
                        print("file",i+1,"could'nt be allocated to any block ","\n")
                               
#=========================================================================================                                        
def best_fit(files,mem):
        print("**********BEST FIT**********")
        print("FILES SIZES","              ","BLOCK-NO","              ","IF")
        no_of_blocks=len(mem)
        no_of_files=len(files)
        flag_m=[0]* no_of_blocks                # 0 is for available
        flag_f=[0]* no_of_files                 # 0 is for not allocated 
        TIF=0
        best=[ ]
        for i in range(no_of_files):
                IF=0
                best=[ ]
                for j in range(no_of_blocks):
                        if flag_m[j]==0 and mem[j]>=files[i] and files[i]>0:
                                best.append(mem[j]-files[i])
                        elif  mem[j]<files[i] or flag_m[j]==1:
                                best.append(10**4)
                                
                index=best.index(min(best))
                
                flag_m[index]=1
                flag_f[i]=1
                IF=mem[index]-files[i]
                TIF+=IF
                print(files[i],"                              ",index+1,"                              ",IF)
                files[i]=0
        print("total Internal fragmentation produced is:  ",TIF,"\n\n")

        for i in range(no_of_files):
                if flag_f[i]==0:
                        print("file",i+1,"could'nt be allocated to any block ","\n")
        
#=========================================================================================
def worst_fit(files,mem):
        print("**********WORST FIT**********")
        print("FILES SIZES","              ","BLOCK-NO","              ","IF")
        no_of_blocks=len(mem)
        no_of_files=len(files)
        flag_m=[0]* no_of_blocks                # 0 is for available
        flag_f=[0]* no_of_files                 # 0 is for not allocated
        #print("flags of mem, files=",flag_m,flag_f)
        TIF=0
        for i in range(no_of_files):
                IF=0
                worst=[ ]
                for j in range(no_of_blocks):
                        if flag_m[j]==0 and mem[j]>=files[i] and files[i]>0:
                                worst.append(mem[j]-files[i])
                        elif  mem[j]<files[i] or flag_m[j]==1:
                                worst.append(10**(-4))
                                #print("10^-4 appended for this process by block ",mem[j])
                                
                if sum(worst)!=(10**(-4))*no_of_blocks:
                        index=worst.index(max(worst))
                        #print(worst)
                        #print("index of worst block is ",index)
                        
                        flag_m[index]=1
                        flag_f[i]=1
                        IF=mem[index]-files[i]
                        TIF+=IF
                        print(files[i],"                              ",index+1,"                              ",IF)
                        files[i]=0
        print("total Internal fragmentation produced is: ",TIF,"\n\n")

        for i in range(no_of_files):
                if flag_f[i]==0:
                        print("file",i+1,"could'nt be allocated to any block \n")
     
#=========================================================================================        
#main code 
mem=list(map(int,input("enter sizes of memory blocks (separated by  spaces) :").split()))               # memory blocks
files=list(map(int,input("Enter sizes  files to be stored (separated by space):  ").split()))           #input files
x=tuple(files)
files2=list(x)
files3=list(x)
#=========================================================================================
first_fit(files,mem)
best_fit(files2,mem)
worst_fit(files3,mem)



