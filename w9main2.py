import math
locations=tuple()
locations=[(37.570295, 126.992078),(37.566550, 126.992679),(37.570169, 126.982856),(37.576549, 126.985520),(37.571618, 126.976551)]
kw=(37.575777,126.973528)
for i in locations:
    import math
    mylist=list()
    distances=[math.sqrt ((i[0]-kw[0])**2+(i[1]-kw[1])**2)]
    mylist.append(distances)
    print min(distances)
    print "Gwanghwamoon"

seoul=list()
seoul=[
    [74425,76326],
    [61164,61636],
    [109688,115744],
    [144796,146776],
    [174996,181676],
    [177841,177434],
    [204630,205980],
    [223373,232245],
    [161055,166130],
    [171576,176735],
    [279169,293772],
    [239450,251066],
    [148690,156510],
    [182977,196992],
    [237792,242641],
    [283869,296762],
    [209344,210282],
    [118965,114441],
    [186503,186856],
    [195734,203014],
    [254381,249472],
    [212401,229111],
    [271654,295354],
    [319197,335045],
    [229829,231671]
    ]
mansum=0
womansum=0
for i in seoul:
    mansum=mansum+i[0]
print "man sum: ",mansum
manaverage=mansum/len(seoul)
print "man average: ",manaverage
for i in seoul:
    womansum=womansum+i[1]
print "womansum: ",womansum
womanaverage=womansum/len(seoul)
print "womanaverage: ",womanaverage
grape=list()
for i in seoul:
    sum=i[0]+i[1]
    y.append(sum)
%matplotlib inline
import matplotlib
import matplotlib.pyplot as plt
plt.bar(range(len(y)),y,align='center')
plt.show
