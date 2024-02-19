def monuments():
  import pandas as pd, matplotlib.pyplot as plt,numpy as np
  a=pd.read_csv('mmts.csv')
  z=np.arange(1,11,1)
  print(a)
  from mpl_toolkits.mplot3d import Axes3D
  fig=plt.figure()
  ax1=fig.add_subplot(1,2,1,projection ='3d')
  l=['Taj Mahal','Red Fort','Qutbminar','Sun temple','Agra Fort','Charminar','Shanirwada',
       'Bibi ka Maqbara','Group of monument','Gol Gumbaz']
  x=[1,2,3,4,5,6,7,8,9,10]
  y=[0,0,0,0,0,0,0,0,0,0]
  z=[0,0,0,0,0,0,0,0,0,0]
  dx=[1,1,1,1,1,1,1,1,1,1]
  dy=[0.01,0.01,0.01,0.01,0.01,0.01,0.01,0.01,0.01,0.01]
  dz=[5653589,3430264,2645070,2461359,1970202,1249039,1247322,1206687,1044091,93917]
  ax1.bar3d(x,y,z,dx,dy,dz,color=['r','y','m','b','c','k','pink','g','violet','beige'])
  ax1.set_xlabel('X')
  ax1.set_ylabel('Y')
  ax1.set_zlabel('Z')
  ax1.set_xticks(x,l,rotation=45)
  ax1.set_title('Domestic visits')
  ax = fig.add_subplot(1, 2, 2, projection='3d')
  x=[1,2,3,4,5,6,7,8,9,10]
  y=[0,0,0,0,0,0,0,0,0,0]
  z=[0,0,0,0,0,0,0,0,0,0]
  dx=[1,1,1,1,1,1,1,1,1,1]
  dy=[0.01,0.01,0.01,0.01,0.01,0.01,0.01,0.01,0.01,0.01]
  dz=[878777,527534,334869,126093,57754,12145,9883,8947,5590,2133]
  ax.bar3d(x,y,z,dx,dy,dz,color=['r','y','m','b','c','k','pink','g','violet','beige'])
  ax.set_xlabel('X')
  ax.set_ylabel('Y')
  ax.set_zlabel('Z')
  ax.set_xticks(x,l,rotation=45)
  ax.set_title('Foreign visits')
  manager= plt.get_current_fig_manager()
  manager.window.state('zoomed')
  plt.show()
  l=['Taj Mahal','Red Fort','Qutbminar','Sun temple','Agra Fort','Charminar','Shanirwada','Bibi ka Maqbara','Group of monument','Gol Gumbaz']
  plt.subplot(2,2,1)
  plt.pie(a.per_do,startangle=65,shadow=True,explode=(0.1,0,0,0,0,0,0,0,0,0),autopct='%1.1f%%')
  plt.legend(l,bbox_to_anchor=(0.05,1), loc="upper left" ,bbox_transform=plt.gcf().transFigure)
  plt.title('Domestic visits')
  plt.subplot(2,2,2)
  plt.pie(a.per_fo,startangle=60,shadow=True,explode=(0.1,0,0,0,0,0,0,0,0,0),autopct='%1.1f%%')
  plt.legend(l,bbox_to_anchor=(0.95,1), loc="upper right" ,bbox_transform=plt.gcf().transFigure)
  plt.title('Foreign visits')
  manager= plt.get_current_fig_manager()
  manager.window.state('zoomed')
  plt.show()
monuments()
