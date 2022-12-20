def optimal_path3(i,j, alignment_matrix,path,depth, indeledSequence1, indeledSequence2,scoreTable):
    residue2=indeledSequence2[i]
    residue1=indeledSequence1[j]
    print(i,j,depth)
    path.append([i,j])
    
    if(i==0 and j==0):
        return
    if(i==0):
        optimal_path3(i,j-1, alignment_matrix,path,depth+1,indeledSequence1,indeledSequence2,scoreTable)
        return
    if(j==0):
        optimal_path3(i-1,j,alignment_matrix,path,depth+1,indeledSequence1,indeledSequence2,scoreTable)
        return
    if(i>0 and j>0):
        up=alignment_matrix[i-1][j]
        left=alignment_matrix[i][j-1]
        diag=alignment_matrix[i-1][j-1]
        maxIndx=np.argmax([up,left,diag])
        if(up==0 and left==0 and diag==0):
            return
        print('argmax=',maxIndx)
        print([up,left,diag])
        if(maxIndx==0):
            optimal_path3(i-1,j, alignment_matrix,path,depth+1,indeledSequence1,indeledSequence2,scoreTable)
        if(maxIndx==1):
            optimal_path3(i,j-1, alignment_matrix,path,depth+1,indeledSequence1,indeledSequence2,scoreTable)
        if(maxIndx==2):
            optimal_path3(i-1,j-1, alignment_matrix,path,depth+1,indeledSequence1,indeledSequence2,scoreTable)
        if(depth==0):
            return path
        else:
            return