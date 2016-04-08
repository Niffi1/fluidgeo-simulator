#!/usr/bin/python
# -*- coding: utf-8 -*-

# Post-processing program to plot results from fluid dynamics
# reservoir problem.
# Author: Diego Volpatto

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import axes3d
from matplotlib import cm
import sys

filepath = sys.argv[1]
filepath2 = sys.argv[2]

#plt.rcParams['legend.loc'] = 'best'
#plt.rc('text', usetex=True)
#plt.rc('font', family='serif')

ano = 30.*12.*86400.
mes = 30.*86400.

# Perfil de pressão

filename = './' + filepath + 'passosPressaoBlocoMacro.dat'
filename2 = './' + filepath2 + 'passosPressaoBlocoMacro.dat'

inDataLegendP = np.loadtxt(filename,unpack=True)
dataLegendP = inDataLegendP[1:]
inDataLegendP2 = np.loadtxt(filename2,unpack=True)
dataLegendP2 = inDataLegendP2[1:]
if (dataLegendP.any() != dataLegendP2.any()):
	sys.exit("Erro: Passos de tempo diferentes")
pnum = len(dataLegendP)
Px0 = np.zeros(pnum)
#pData = np.loadtxt('./expTeste/fort.1111',unpack=True)
#Pr = pData[0]
#Pw = pData[1]
#PI = pData[2]

fig = plt.figure()
#ax = fig.gca(projection='3d')

#ax = fig.adsd_subplot(111, projection='3d')

ax = plt.subplot(111)

for i in range(1,pnum+1):
    #i_mask = 10*i
    inDataNameP = './' + filepath + ('solP_C.%d' % i)
    inDataNameP2 = './' + filepath2 + ('solP_C.%d' % i)
    xx, yy, P = np.loadtxt(inDataNameP,unpack=True,usecols=[2,3,4])
    xx2, yy2, P2 = np.loadtxt(inDataNameP2,unpack=True,usecols=[2,3,4])
    #print xx
    #print yy
    #print P
    #fig = plt.figure()
    #ax = fig.gca(projection='3d')
    #ax = fig.add_subplot(111, projection='3d')
    
    if dataLegendP[i-1] == 1.:
        leg = (u"%d mês" % dataLegendP[i-1])
    else:
        leg = ("%d meses" % dataLegendP[i-1])
    Px0[i-1] = P[0]
    #ax.plot(xx,yy,P,'o',label=leg)
    ax.plot(xx,P,'-',label=leg)
    #ax.plot(xx2,P2,label=leg)
    ax.plot(xx2,P2,'-.')

box = ax.get_position()
ax.set_position([box.x0, box.y0, box.width * 0.8, box.height])
ax.legend(loc='center left', bbox_to_anchor=(1, 0.5))
ax.set_xlabel(r'$x$',fontsize=18)
#ax.set_ylabel('$y^{*}$',fontsize=18)
ax.set_ylabel(r'$p$',fontsize=18)
ax.grid(True)

plt.savefig('./' + filepath + 'tmpPressaoC_comp.png')
#plt.show()

fig = plt.figure()
#ax = fig.gca(projection='3d')

#ax = fig.adsd_subplot(111, projection='3d')

ax = plt.subplot(111)

for i in range(1,pnum+1):
    #i_mask = 10*i
    inDataNameP = './' + filepath + ('solP_BC.%d' % i)
    inDataNameP2 = './' + filepath2 + ('solP_BC.%d' % i)
    xx, yy, P = np.loadtxt(inDataNameP,unpack=True,usecols=[2,3,4])
    xx2, yy2, P2 = np.loadtxt(inDataNameP,unpack=True,usecols=[2,3,4])
    #print xx
    #print yy
    #print P
    #fig = plt.figure()
    #ax = fig.gca(projection='3d')
    #ax = fig.add_subplot(111, projection='3d')
    
    if dataLegendP[i-1] == 1.:
        leg = (u"%d mês" % dataLegendP[i-1])
    else:
        leg = ("%d meses" % dataLegendP[i-1])
    Px0[i-1] = P[0]
    #ax.plot(xx,yy,P,'o',label=leg)
    ax.plot(xx,P,label=leg)
    ax.plot(xx2,P2,'-.')

box = ax.get_position()
ax.set_position([box.x0, box.y0, box.width * 0.8, box.height])
ax.legend(loc='center left', bbox_to_anchor=(1, 0.5))
ax.set_xlabel(r'$x$',fontsize=18)
#ax.set_ylabel('$y^{*}$',fontsize=18)
ax.set_ylabel(r'$p$',fontsize=18)
ax.grid(True)

plt.savefig('./' + filepath + 'tmpPressaoBC_comp.png')
#plt.show()


fig = plt.figure()
#ax = fig.gca(projection='3d')

#ax = fig.add_subplot(111, projection='3d')

ax = plt.subplot(111)

for i in range(1,pnum+1):
    #i_mask = 11*i
    inDataNameGradP = './' + filepath + ('gradPx.%d' % i)
    inDataNameGradP2 = './' + filepath2 + ('gradPx.%d' % i)
    xx, yy, gradP = np.loadtxt(inDataNameGradP,unpack=True,usecols=[2,3,4])
    xx2, yy2, gradP2 = np.loadtxt(inDataNameGradP2,unpack=True,usecols=[2,3,4])
    #print xx
    #print yy
    #print gradP
    #fig = plt.figure()
    #ax = fig.gca(projection='3d')
    #ax = fig.add_subplot(111, projection='3d')
    if dataLegendP[i-1] == 1.:
        leg = (u"%d mês" % dataLegendP[i-1])
    else:
        leg = ("%d meses" % dataLegendP[i-1])
    Px0[i-1] = P[0]
    #ax.plot(xx,yy,gradP,'o',label=leg)
    ax.plot(xx,gradP,'-',label=leg)
    ax.plot(xx2,gradP2,'-.')
    #surf = ax.plot_surface(xx, yy, P, rstride=1, cstride=1, cmap=cm.coolwarm,
        #linewidth=0, antialiased=True)
    #surf = ax.plot_surface(xx, yy, P)
    #plt.show()
    #plt.pcolor(xx,yy,P)
    #ax.contour(xx, yy, P)
    #plt.savefig('./teste/tmpPressao%d.png' % i_mask)

box = ax.get_position()
ax.set_position([box.x0, box.y0, box.width * 0.8, box.height])
ax.legend(loc='center left', bbox_to_anchor=(1, 0.5))
ax.set_xlabel(r'$x$',fontsize=18)
#ax.set_ylabel('$y^{*}$',fontsize=18)
ax.set_ylabel(r"$\nabla p$",fontsize=18)
#plt.xlabel('$x^{*}$',fontsize=18)
#plt.ylabel('$p^{*}$',fontsize=18,rotation='horizontal')
#plt.grid(b=True, which='major', color='k', linestyle='--')
#ax.legend()
plt.grid(True)
plt.savefig('./' + filepath + 'tmpgradPressao_comp.png')
#plt.show()

fig = plt.figure()
#ax = fig.gca(projection='3d')

#ax = fig.add_subplot(111, projection='3d')

ax = plt.subplot(111)

for i in range(1,pnum+1):
    #i_mask = 14*i
    inDataNameV = './' + filepath + ('solVelocity_x.%d' % i)
    inDataNameV2 = './' + filepath2 + ('solVelocity_x.%d' % i)
    xx, yy, V = np.loadtxt(inDataNameV,unpack=True,usecols=[2,3,4])
    xx2, yy2, V2 = np.loadtxt(inDataNameV2,unpack=True,usecols=[2,3,4])
    #print xx
    #print yy
    #print V
    #fig = plt.figure()
    #ax = fig.gca(projection='3d')
    #ax = fig.add_subplot(111, projection='3d')
    if dataLegendP[i-1] == 1.:
        leg = (u"%d mês" % dataLegendP[i-1])
    else:
        leg = ("%d meses" % dataLegendP[i-1])
    Px0[i-1] = P[0]
    #ax.plot(xx,yy,V,'o',label=leg)
    ax.plot(xx,V,'-',label=leg)
    ax.plot(xx2,V2,'-.')
    #surf = ax.plot_surface(xx, yy, P, rstride=1, cstride=1, cmap=cm.coolwarm,
        #linewidth=0, antialiased=True)
    #surf = ax.plot_surface(xx, yy, P)
    #plt.show()
    #plt.pcolor(xx,yy,P)
    #ax.contour(xx, yy, P)
    #plt.savefig('./teste/tmpPressao%d.png' % i_mask)

box = ax.get_position()
ax.set_position([0.45*box.x0+box.x0, box.y0, box.width * 0.7, box.height])
ax.legend(loc='center left', bbox_to_anchor=(1, 0.5))
#ax.legend(loc='best')
ax.set_xlabel(r'$x$',fontsize=18)
#ax.set_ylabel('$y^{*}$',fontsize=18)
ax.set_ylabel(r"$u_D\,(m/s)$",fontsize=18)
#plt.xlabel('$x^{*}$',fontsize=18)
#plt.ylabel('$p^{*}$',fontsize=18,rotation='horizontal')
#plt.grid(b=True, which='major', color='k', linestyle='--')
#ax.legend()
plt.grid(True)
plt.savefig('./' + filepath + 'tmpV_comp.png')
#plt.show()

fig = plt.figure()
#ax = fig.gca(projection='3d')

#ax = fig.add_subplot(111, projection='3d')

ax = plt.subplot(111)

'''
for i in range(1,pnum+1):
    #i_mask = 19*i
    inDataNameJ = './' + filepath + ('nodeFlux_x.%d' % i)
    inDataNameJ2 = './' + filepath2 + ('nodeFlux_x.%d' % i)
    xx, yy, J = np.loadtxt(inDataNameJ,unpack=True,usecols=[2,3,4])
    xx2, yy2, J2 = np.loadtxt(inDataNameJ2,unpack=True,usecols=[2,3,4])
    #print xx
    #print yy
    #print J
    #fig = plt.figure()
    #ax = fig.gca(projection='3d')
    #ax = fig.add_subplot(111, projection='3d')
    if dataLegendP[i-1] == 1.:
        leg = (u"%d mês" % dataLegendP[i-1])
    else:
        leg = ("%d meses" % dataLegendP[i-1])
    Px0[i-1] = P[0]
    #ax.plot(xx,yy,J,'.',label=leg)
    #ax.plot(xx,yy,J,'o',label=leg)
    ax.plot(xx,J,'-',label=leg)
    ax.plot(xx2,J2,'-.')
    #surf = ax.plot_surface(xx, yy, P, rstride=1, cstride=1, cmap=cm.coolwarm,
        #linewidth=0, antialiased=True)
    #surf = ax.plot_surface(xx, yy, P)
    #plt.show()
    #plt.pcolor(xx,yy,P)
    #ax.contour(xx, yy, P)
    #plt.savefig('./teste/tmpPressao%d.png' % i_mask)

box = ax.get_position()
ax.set_position([0.45*box.x0+box.x0, box.y0, box.width * 0.8, box.height])
#ax.legend(loc='center left', bbox_to_anchor=(1, 0.5))
ax.legend(loc='best')
ax.set_xlabel('$x$',fontsize=18)
#ax.set_ylabel(r'$y^{*}$',fontsize=18)
ax.set_ylabel(r'$J \,\left(\frac{kg}{m^2 s}\right)$',fontsize=18)
#plt.xlabel('$x^{*}$',fontsize=18)
#plt.ylabel('$p^{*}$',fontsize=18,rotation='horizontal')
#plt.grid(b=True, which='major', color='k', linestyle='--')
#ax.legend()
plt.grid(True)
plt.savefig('./' + filepath + 'tmpJ_comp.png')
#plt.show()

fig = plt.figure()
#ax = fig.gca(projection='3d')

#ax = fig.add_subplot(111, projection='3d')

ax = plt.subplot(111)


for i in range(1,pnum+1):
    #i_mask = 23*i
    inDataNameResid = './' + filepath + ('residueFlux_x.%d' % i)
    inDataNameResid2 = './' + filepath2 + ('residueFlux_x.%d' % i)
    xx, yy, Resid = np.loadtxt(inDataNameResid,unpack=True,usecols=[2,3,4])
    xx2, yy2, Resid2 = np.loadtxt(inDataNameResid2,unpack=True,usecols=[2,3,4])
    #print xx
    #print yy
    #print Resid
    #fig = plt.figure()
    #ax = fig.gca(projection='3d')
    #ax = fig.add_subplot(111, projection='3d')
    if dataLegendP[i-1] == 1.:
	leg = (u"%d mês" % dataLegendP[i-1])
    else:
	leg = ("%d meses" % dataLegendP[i-1])
    Px0[i-1] = P[0]
    #ax.plot(xx,yy,J,'.',label=leg)
    #ax.plot(xx,yy,J,'o',label=leg)
    ax.plot(xx,Resid,'-',label=leg)
    ax.plot(xx2,Resid2,'-.')
    #surf = ax.plot_surface(xx, yy, P, rstride=1, cstride=1, cmap=cm.coolwarm,
        #linewidth=0, antialiased=True)
    #surf = ax.plot_surface(xx, yy, P)
    #plt.show()
    #plt.pcolor(xx,yy,P)
    #ax.contour(xx, yy, P)
    #plt.savefig('./teste/tmpPressao%d.png' % i_mask)

box = ax.get_position()
ax.set_position([0.2*box.x0+box.x0, box.y0, box.width * 0.8, box.height])
ax.legend(loc='center left', bbox_to_anchor=(1, 0.5))
ax.set_xlabel('$x$',fontsize=18)
#ax.set_ylabel(r'$y^{*}$',fontsize=18)
ax.set_ylabel(u'Resíduo',fontsize=18)
#plt.xlabel('$x^{*}$',fontsize=18)
#plt.ylabel('$p^{*}$',fontsize=18,rotation='horizontal')
#plt.grid(b=True, which='major', color='k', linestyle='--')
#ax.legend()
plt.grid(True)
plt.savefig('./' + filepath + 'tmpResid_comp.png')
#plt.show()
'''
## Produção do bloco
fig = plt.figure()
#ax = fig.gca(projection='3d')

#ax = fig.add_subplot(111, projection='3d')

ax = plt.subplot(111)

inDataNameJprod = './' + filepath + 'echoProducao.dat'
inDataNameJprod2 = './' + filepath2 + 'echoProducao.dat'
dt, Jprod = np.loadtxt(inDataNameJprod,unpack=True,usecols=[1,5])
dt2, Jprod2 = np.loadtxt(inDataNameJprod2,unpack=True,usecols=[1,5])
dt = dt/mes
dt2 = dt2/mes
ax.set_xlabel(r'$t\,(meses)$',fontsize=18)
ax.set_ylabel(r'$Produ \c c \~ a o\, \left(kg\right)$',fontsize=16)
ax.plot(dt,Jprod,'-',label=u'Produção')
ax.plot(dt2,Jprod2,'-.')
box = ax.get_position()
ax.set_position([0.1*box.x0+box.x0, box.y0, box.width * 0.8, box.height])
ax.legend(loc='center left', bbox_to_anchor=(1, 0.5))
plt.grid(True)
plt.savefig('./' + filepath + 'Prod_comp.png')
#plt.show()

# RF barra
fig = plt.figure()
#ax = fig.gca(projection='3d')

#ax = fig.add_subplot(111, projection='3d')

ax = plt.subplot(111)

inDataNameRF_ = './' + filepath + 'echoProducao.dat'
inDataNameRF_2 = './' + filepath2 + 'echoProducao.dat'
dt, RF_ = np.loadtxt(inDataNameRF_,unpack=True,usecols=[1,6])
dt2, RF_2 = np.loadtxt(inDataNameRF_2,unpack=True,usecols=[1,6])
dt = dt/mes
dt2 = dt2/mes
ax.set_xlabel(r'$t\,(meses)$',fontsize=18)
ax.set_ylabel(r'$RF_{recuper\'avel}$',fontsize=16)
ax.plot(dt,RF_,'-',label=u'RF')
ax.plot(dt2,RF_2,'-.')
box = ax.get_position()
ax.set_position([0.1*box.x0+box.x0, box.y0, box.width * 0.8, box.height])
ax.legend(loc='center left', bbox_to_anchor=(1, 0.5))
plt.grid(True)
plt.savefig('./' + filepath + 'RF_comp.png')
#plt.show()

# RF
fig = plt.figure()
#ax = fig.gca(projection='3d')

#ax = fig.add_subplot(111, projection='3d')

ax = plt.subplot(111)

inDataNameRF = './' + filepath + 'echoProducao.dat'
inDataNameRF2 = './' + filepath2 + 'echoProducao.dat'
dt, RF = np.loadtxt(inDataNameRF,unpack=True,usecols=[1,7])
dt2, RF2 = np.loadtxt(inDataNameRF2,unpack=True,usecols=[1,7])
dt = dt/mes
dt2 = dt2/mes
ax.set_xlabel(r'$t\,(meses)$',fontsize=18)
ax.set_ylabel(r'$RF_{total}$',fontsize=16)
ax.plot(dt,RF,'-',label=u'RF')
ax.plot(dt2,RF2,'-.')
box = ax.get_position()
ax.set_position([0.1*box.x0+box.x0, box.y0, box.width * 0.8, box.height])
ax.legend(loc='center left', bbox_to_anchor=(1, 0.5))
plt.grid(True)
plt.savefig('./' + filepath + 'RFcomp.png')
#plt.show()

fig = plt.figure()
#ax = fig.gca(projection='3d')

#ax = fig.add_subplot(111, projection='3d')

ax = plt.subplot(111)

#inDataNameRF = './' + filepath + 'echoProducao.dat'
dt, Flux = np.loadtxt(inDataNameRF,unpack=True,usecols=[1,3])
dt2, Flux2 = np.loadtxt(inDataNameRF2,unpack=True,usecols=[1,3])
dt = dt/mes
dt2 = dt2/mes
ax.set_xlabel(r'$t\,(meses)$',fontsize=18)
ax.set_ylabel(r'J $\left(\frac{kg}{m^2 s}\right)$',fontsize=16)
ax.plot(dt,Flux,'-',label=u'Fluxo Mássico')
ax.plot(dt2,Flux2,'-.')
box = ax.get_position()
ax.set_position([0.45*box.x0+box.x0, box.y0, box.width * 0.95, box.height])
#ax.legend(loc='center left', bbox_to_anchor=(1, 0.5))
ax.legend(loc='best')
plt.grid(True)
plt.savefig('./' + filepath + 'Fluxo.png')
#plt.show()

print "Comparative pressure's plots OK"