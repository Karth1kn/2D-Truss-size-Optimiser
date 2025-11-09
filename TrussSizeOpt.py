import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import fsolve, root
#import sympy as sp
import scipy.linalg as slin
import time
import math



#trails()
area= np.array([1,1,0.3]) #m**2
youngs_modulus= 20.0 #N/m**2
yield_stress= 3 #N\m**2
const= area*youngs_modulus
sequence = [0,1,2,3]
max_disp = 0.1


#jeff hanson
cord = np.array([[0.0,0.0],[0.0,4.0],[3.0,0.0], [4.0,0.0]])
con = np.array([[0,1], [0,2], [1,2], [1,3], [2,3]])
bc_lst = [0,1, 7]
force= np.array([[1, 5.0, 0.0], 
        [2, 0.0,-8.0]])
sequence = [0,1,2,3]

#jeff hanson howe truss
cord = np.array([[0,0],[2,2],[2,0],[4,0],[4,2],[6,2],[6,0],[8,0]])
con = np.array([[0,1],[0,2],[1,2],[1,4],[2,4],[2,3],[3,4],[3,6],[4,5],[4,6],[5,6],[5,7],[6,7]])
bc_lst = [0,1 , 15]
force = np.array([[2, 0, -9], [3, 0, -4], [6, 0, -7]])
unitforce = np.array([[1, 0.0, 0.0],
                  [3, 0.0, -1.0]])
sequence = [0,1,2,3,4,5,6,7]

#jeff hanson pratt truss
cord = np.array([[0,0], [2,0],[2,2],[4,4],[4,0],[6,6],[6,0],[8,4],[8,0],[10,2],[10,0],[12,0]])
con = np.array([[0,1],[0,2],[1,2],[2,4],[1,4],[2,3],[3,4],[3,6],[4,6],[3,5],[5,6],[5,7],[6,7],[6,8],[7,8],[7,9],[8,9],[8,10],[9,10],[9,11],[10,11]])
print(len(con))
force = np.array([[4, 0, -10],[6, 0, -20], [8, 0, -10]])
unitforce = np.array([[1, 0.0, 0.0],
                  [6, 0.0, -1.0]])
bc_lst= [0,1 , 23]
sequence = [0,1,2,4,3,5,6,7,8,9,10,11]

""" #Lecture 3 Slides
cord = np.array([[0.0,0.0], [1.5,2.6], [3.0,0.0], [4.5,2.6], [6.0,0.0]])
#cord = np.array([[0.0,0.0], [0.5,1.0], [1.0,0.0], [1.5,1.0], [2.0,0.0]])
con = np.array([[0,1],[1,2],[0,2],[1,3],[2,3],[3,4],[2,4]])
bc_lst = [0,1, 9]
force = np.array([[1, 5.0, -10.0],
                  [3, 0.0, -15.0]])
unitforce = np.array([[1, 0.0, 0.0],
                  [2, 0.0, -1.0]])
#force = np.array([[1, 0.0, 0.0],[3, 0.0, -200.0]])
#force = np.array([[1, 0.0, 0.0],[2, 0.0, -1.0]])
sequence = [0,1,2,3,4] """

""" #Assignemnt problem
cord = np.array([[0.0,0.0], [3.0,0.25], [5.0,1.0], [6.0,2.0], [5.0,3.0], [3.0,3.75], [0.0,4.0]])
con = np.array([[0,1],[1,2],[2,3],[3,4], [4,5], [5,6], [6,1], [5,0], [5,2], [4,1]])
bc_lst = [0,1 , 12,13]
force = np.array([[5, 0.0, -4.0], [3, 0.0, -2.0], [2, 0.0, -4.0]])
unitforce = np.array([[3, 0.0, -1.0]])
sequence = [0,6, 5,1,4,3,2] """
#sequence = [0,6]

#Youtube problem
""" cord = np.array([[0.0,0.0], [0.5,0.866], [1.0,0.0], [1.5,0.866], [2.0,0.0], [2.5,0.866], [3.0,0.0]])
#cord = np.array([[0.0,0.0], [0.5,1.0], [1.0,0.0], [1.5,1.0], [2.0,0.0]])
con = np.array([[0,1],[1,2],[0,2],[1,3],[2,3],[3,4],[2,4],[3,5],[4,5],[5,6],[4,6]])
bc_lst = [0,1, 13]
force = np.array([[2, 0.0, -100.0],
                  [4, 0.0, -50.0]])
unitforce = np.array([[1, 0.0, 0.0],
                  [4, 0.0, -1.0]])
sequence = [0,1,2,3,4,5,6] """


""" cord = np.array([[0,0], [2,0], [4,0],[4,2], [2,2], [0,2]])
con = np.array([[0,1],[1,2],[2,3],[3,4],[4,5],[0,5], [0,4], [4,2], [1,4]])
force = np.array([[1, 0.0, -20.0], [3, -15.0, 0.0], [4, 0.0, -10.0], [5, 0.0, -25.0]])
bc_lst = [1,2 ,5]
sequence = [1,0,2,3,4,5] """

def Pplotter(coordinate):
    for i in force:
        continue
        #plt.arrow(*cord[i[0]], 0.1*i[1], 0.1*i[2], width = 0.01, head_width = 0.1)
    for i,k in enumerate(con):
        r,b = 0,0
        kj=[coordinate[k[0]],coordinate[k[1]]]
        c=[kj[0][0],kj[1][0]]
        d=[kj[0][1],kj[1][1]]
        plt.plot(c,d, color = 'red')
        plt.text(kj[0][0], kj[0][1], f"{k[0]}")
        plt.text(kj[1][0], kj[1][1], f"{k[1]}")
        plt.text((kj[0][0]+kj[1][0])/2, (kj[0][1]+kj[1][1])/2, f"{i}", color = 'blue')
    plt.show()

#Pplotter(cord)

def force_matrix(node,force):
    f_matrix= np.zeros([2*len(cord),1])
    f_matrix[2*(node)] += force[0]
    f_matrix[2*(node)+1] += force[1]
    return f_matrix

force_mat=force_matrix(0,[0,0])
for ac in force:
    force_mat += force_matrix(int(ac[0]),ac[1:])

force_matc =force_matrix(0,[0,0])
for ac in force:

    force_matc += force_matrix(int(ac[0]),ac[1:])



def ln(node1,node2,corl):
    n1= node1
    n2= node2
    return abs((( corl[(n2),0] - corl[(n1),0] )**2 + ( corl[(n2),1] - corl[(n1),1] )**2 )**0.5)

#print(ln(2,3))
def cos(node1,node2,type):
    if node1>node2:
        #node1,node2 = node2,node1
        pass
    return ((type[node2,0]-type[node1,0])/ln(node1,node2,type))

#print(cos(1,2))
def sin(node1, node2,type):
    if node1>node2:
        #node1,node2 = node2,node1
        pass
    return ((type[node2,1]-type[node1,1])/ln(node1,node2,type))

dcord = np.copy(cord)


def moments(Piv):
    mom = 0
    for i, val in enumerate(force):
        dy = (cord[int(force[i,0]),1] - Piv[1])

        mom -= force[i, 1]*(cord[int(force[i,0]),1] - Piv[1]) #mom for x forces
        mom += force[i, 2]*(cord[int(force[i,0]),0] - Piv[0]) #mom for Y forces
    return mom

def momMat(Piv, n):
    momMat = np.zeros([1,n])
    #ps = np.unique([(i-i%2)/2 for i in bc_lst])
    for i,val in enumerate(bc_lst):
        if bc_lst[i]%2 == 0:
            momMat[0,i] = -(cord[int((val-val%2)/2) ,1] - Piv[1])
        else: 
            momMat[0,i] = (cord[int((val-val%2)/2) ,0] - Piv[0])

    return momMat


#print(moments(cord[0]))
#print(momMat(cord[3], 3))
def reactions():
    if 2*len(cord) > len(con)+len(bc_lst):
        print("Statically indeterminate")
        return 0
    elif 2*len(cord) < len(con)+len(bc_lst):
        print("Unstable structure. Matrix will be singular")
        return 0
    elif 2*len(cord) == len(con)+len(bc_lst):
        print("STATICALLY DETERMINATE")
        uRxn = len(bc_lst) # No of Unknown reactions
        #sol = [Ax, Ay, Cy] in order
        pivots = cord[np.unique([int((i-i%2)/2) for i in bc_lst]),:]
        
        #force equations
        Rx = np.zeros([uRxn, uRxn])
        for i in range(uRxn):
            if bc_lst[i]%2 == 0:
                Rx[0,i] = 1
                Rx[1,i] = 0
            else:
                Rx[0,i] = 0
                Rx[1,i] = 1

        #moment equations
        #p = pivots[0]
        #mom = moments(p)
        #Rx[2,:] = momMat(p, uRxn)


        #F = np.array([[-np.sum(force[:, 1]), -np.sum(force[:, 2]), -mom]])
        F = np.zeros([1,uRxn])

        F[0,0], F[0,1] = -np.sum(force[:, 1]), -np.sum(force[:, 2])
        for i in range(uRxn-2):
            #continue
            p = pivots[i]
            mom = moments(p)
            Rx[i+2:] = momMat(p, uRxn)
            F[0,2+i] = -mom

        #print(Rx,F)
        sol = np.linalg.pinv(Rx) @ F.T#np.linalg.inv(Rx)@F.T
        #print(sol)
        return sol

#reactions()
#print(reactions())

def memberAngle(pivot,point):
    member = cord[point] - cord[pivot]
    #angle = member[0]/ln(point, pivot, cord)
    angle = np.degrees(np.arctan2(member[1], member[0]))
    if angle<0:
        angle = 360+angle
    return angle

ang = memberAngle(1,0)


Members = np.zeros([2,len(con)])
ReactionForces = np.zeros([1,2*len(cord)])
ExternalForces = force_matc.T.reshape(len(cord), 2)
ReactionForces[0,bc_lst] = reactions()[:,0]
memberAreas = np.zeros([1,len(con)])

#print(ExternalForces)
#pA = [Rx,Ry, Mx, My, Ex, Ey]
# point = n, Members = [[point1, pivot1], [point2, pivot1]....], Reactions = [Fx, Fy], ExtFor = [Fx, fy], MemFor = [F1, F2,....]

Mf = np.zeros([1,len(con)])
UMf = np.zeros([1,len(con)])

def plotter(coordinate, Mf):
    Mf = np.round(Mf,3)

    MMax = max(abs(Mf[0]))
    fig, ax = plt.subplots()

    for i,k in enumerate(con):
        r,b = 0,0
        k=[coordinate[k[0]],coordinate[k[1]]]
        c=[k[0][0],k[1][0]]
        d=[k[0][1],k[1][1]]
        plt.text((k[0][0]+k[1][0])*0.5, (k[0][1]+k[1][1])*0.5, f'{Mf[0,i]}', color = "white")
        if Mf[0,i]>=0:
            r = abs(Mf[0,i]/MMax)
            plt.plot(c,d,color=(1,1-r,1-r), linewidth = 2)
        if Mf[0,i]<0:
            b =abs( Mf[0,i]/MMax)
            plt.plot(c,d,color=(1-b,1-b,1), linewidth = 2)

        ax.set_facecolor('black')



def pivotFr(pivot, Reactions, ExtFor, MemberForces):
    Members =  np.array([i for i in con if pivot in i]) #members in con connected to ppivot
    Memind = np.array([np.where(np.all(con == i, axis=1))[0] for i in con if pivot in i]).T[0]

    #print(Memind, "memind")
    UMembers= [con[i] for i in Memind if MemberForces[0,i] == 0.0]
    Um = [i for i in Memind if MemberForces[0,i] == 0.0]
    KMembers = [con[i] for i in Memind if MemberForces[0,i] != 0.0]
    def Orienter(Members):
        for i in Members:
            if i[0] != pivot:
                i[0], i[1] = i[1], i[0]
        return Members

    UMembers= Orienter(UMembers)
    KMembers =Orienter(KMembers)
    #print(pivot, "Pivot", Members, "members")

    Km = [i for i in Memind if MemberForces[0,i] != 0.0]
    if len(UMembers)==1:
        alpha = np.radians(memberAngle(*UMembers[0]))
        F = -Reactions[0,2*pivot] - ExtFor[0]
        for i, mem in enumerate(Km):
            F -= MemberForces[0,mem]*np.cos(np.radians(memberAngle(*KMembers[i])))

        Fint = F/np.cos(alpha)
        if MemberForces[0,Um[0]] == 0.0:
            MemberForces[0,Um[0]] = Fint
    if len(UMembers)==2:
        theta = np.radians(memberAngle(*UMembers[0]))
        phi = np.radians(memberAngle(*UMembers[1]))

        #print(memberAngle(*UMembers[0]), memberAngle(*UMembers[1]), "theta, phi")
        #print(Memind)
        
        #print(UMembers, KMembers, "UK") 
        #print(ExtFor, "extfor")

        K = np.array([[np.cos(theta), np.cos(phi)],
                    [np.sin(theta), np.sin(phi)]])
        F = np.array([[-Reactions[0,2*pivot] - ExtFor[0] ],
                    [-Reactions[0,2*pivot+1] - ExtFor[1]]])
        #print(Reactions[0,2*pivot:2*pivot+2], ExtFor, "react extfor")

        #print('Equilibrium Matrix',K)
        for i, mem in enumerate(Km):

            F[0,0] -= MemberForces[0,mem]*np.cos(np.radians(memberAngle(*KMembers[i])))
            F[1,0] -= MemberForces[0,mem]*np.sin(np.radians(memberAngle(*KMembers[i])))
        #print(K,F,'final')
        #print(K, F, "JKKKK")

        Forces = np.linalg.inv(K)@F
        #print(Forces, "Forces")
        for i, val in enumerate(Forces):
            if MemberForces[0,Um[i]] == 0.0:
                MemberForces[0,Um[i]] = val[0]
    elif len(UMembers)>2:
        print(f'unknown member at {pivot}. Try different sequence')
        return 0

              



for i in sequence:
    #continue
    pivot = i
    pivotFr(pivot, ReactionForces, ExternalForces[pivot],Mf)





#finding displacements for unti load
force = unitforce
force_matc=force_matrix(0,[0,0])
for ac in force:
    force_matc += force_matrix(int(ac[0]),ac[1:])
ExternalForces = force_matc.T.reshape(len(cord), 2)
ReactionForces = np.zeros([1,2*len(cord)])
ReactionForces[0,bc_lst] = reactions()[:,0]

for i in sequence:
    #continue
    pivot = i
    pivotFr(pivot, ReactionForces, ExternalForces[pivot],UMf)

#Optimisation

summ = 0
for i in range(len(con)):
    summ += ((abs(UMf[0,i])*abs(Mf[0,i])/(youngs_modulus))**0.5)*ln(*con[i], cord)

Lambda = (summ/(max_disp*1e3))**2



for i in range(len(memberAreas[0])):
    #print(math.sqrt(Lambda*Mf[0,i]*UMf[0,i]/youngs_modulus))
    memberAreas[0,i] = math.sqrt(Lambda*abs(UMf[0,i])*abs(Mf[0,i])/(youngs_modulus))

#print(Lambda,memberAreas)

def forcesplotter(coordinate,Mf):
    Mf = np.round(Mf,3)

    MMax = max(abs(Mf[0]))
    fig, ax = plt.subplots()
    plt.title("Member Forces")
    for i,k in enumerate(con):
        r,b = 0,0
        k=[coordinate[k[0]],coordinate[k[1]]]
        c=[k[0][0],k[1][0]]
        d=[k[0][1],k[1][1]]
        plt.text((k[0][0]+k[1][0])*0.5, (k[0][1]+k[1][1])*0.5, f'{Mf[0,i]}', color = "white")
        if Mf[0,i]>=0:
            r = abs(Mf[0,i]/MMax)
            plt.plot(c,d,color=(1,1-r,1-r), linewidth = 2)
        if Mf[0,i]<0:
            b =abs( Mf[0,i]/MMax)
            plt.plot(c,d,color=(1-b,1-b,1), linewidth = 2)

        ax.set_facecolor('black')


def areaplotter(coordinate,Mf):
    Mf = np.round(Mf,3)
    maxwidth = 10
    maxarea = max(memberAreas[0])
    MMax = max(abs(Mf[0]))
    fig, ax = plt.subplots()
    plt.title("Optimised Areas")
    for i,k in enumerate(con):
        r,b = 0,0
        k=[coordinate[k[0]],coordinate[k[1]]]
        c=[k[0][0],k[1][0]]
        d=[k[0][1],k[1][1]]
        plt.text((k[0][0]+k[1][0])*0.5, (k[0][1]+k[1][1])*0.5, f'{round(memberAreas[0,i],4)}', color = "white")
        if Mf[0,i]>=0:
            r = abs(Mf[0,i]/MMax)
            plt.plot(c,d,color=(1,1-r,1-r), linewidth = (memberAreas[0,i]/maxarea)*maxwidth)
        elif Mf[0,i]<0:
            b =abs( Mf[0,i]/MMax)
            plt.plot(c,d,color=(1-b,1-b,1), linewidth = (memberAreas[0,i]/maxarea)*maxwidth)
        if (memberAreas[0,i]/maxarea) < 1e-3:
            b =abs( Mf[0,i]/MMax)
            plt.plot(c,d,color=(1-b,1-b,1), linewidth = 2)

        ax.set_facecolor('black')

forcesplotter(cord, Mf)
plotter(cord,UMf)
areaplotter(cord,Mf)

def disturbance(d):
    delta = 0
    memberAreas[0,1] += d

    for i in range(len(con)):
        delta += (UMf[0,i]*Mf[0,i]*ln(*con[i], cord))/(memberAreas[0,i]*youngs_modulus*1e3)

    #print("Displacement of point before changing values: ",delta)
    memberAreas[0,1] -= d
    return delta

""" de=0
for i in range(len(con)):
        de += (UMf[0,i]*Mf[0,i]*ln(*con[i], cord))/(memberAreas[0,i]*youngs_modulus*1e3)
fig,ax = plt.subplots()
plt.scatter(0,de, color= 'red', s=15)
plt.text(0,de, "actual deflection in my code without changing any value")
n=5
for i in np.linspace(-n,n,100):
    plt.scatter(i, disturbance(i), s=10, color= 'blue')
    plt.xlabel('disturbance given to the final area of member 4')
    plt.ylabel('corresponding change in the deflection of the point')
 """
plt.show()

