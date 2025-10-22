inputs=[1,2,3,2.5]
weights=[[0.2,0.8,-0.5,1],[0.5,-0.91,0.26,-0.5]
,[-0.26,-0.27,0.17,0.87]]
bias=[2,3,0.5]


layer_outputs=[]
for i in range(len(weights)):
    sum=0
    for j in range(len(weights[i])):
        sum+=inputs[j]*weights[i][j]
    sum+=bias[i]
    layer_outputs.append(sum)    


print(layer_outputs)