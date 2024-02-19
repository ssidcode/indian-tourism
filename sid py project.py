#1.Inbound Tourism: Foreign Tourist Arrivals (FTAs), Arrivals of Non-Resident Indians (NRIs)
#and International Tourist Arrivals (ITAs)
def inbound():
  import pandas as pd, matplotlib.pyplot as plt,numpy as np
  a=pd.read_csv('ia.csv')
  s=pd.DataFrame(a)
  l=np.arange(1,20,2)
  print(s)
  x=[2014,2015,2016,2017,2018]
  FTA=[7.68,8.03,8.80,10.04,10.56]
  NRI=[5.43,5.74,6.22,6.77,6.87]
  ITA=[13.11,13.76,15.03,16.81,17.42]
  b=['FTA','nri','intarrival']
  p=plt.bar(a.year,a.FTA,width=0.25,color='b')
  j=plt.bar(a.year+0.25,a.nri,width=0.25,color='g')
  k=plt.bar(a.year+0.5,a.intarrival,width=0.2,color='m')
  fd={'family':'monotype corsiva','color':'k','size':'20','weight':'bold'}
  plt.ylabel('global tourist arrivals',fontdict=fd,labelpad=5)
  plt.xlabel('years',fontdict=fd,labelpad=5)
  plt.title('Inbound Tourism',fontdict=fd,pad=20)
  plt.xticks(a.year)
  plt.legend(['FTA','NRI','ITA'])
  plt.show()

#2:2.1 SEASONALITY IN FOREIGN TOURIST ARRIVALS IN India
def seasonality():
  import matplotlib.pyplot as plt, numpy as np ,pandas as pd
  a=pd.read_csv('seasonal.csv')
  print(a) 
  b=(1,20,6)
  fd={'family':'monotype corsiva','color':'k','size':'20','weight':'bold'}
  plt.bar(a.year,a.jan,width=0.08,color='y')
  plt.bar(a.year+0.16,a.feb,width=0.08,color='r')
  plt.bar(a.year+0.24,a.march,width=0.08,color='b')
  plt.bar(a.year+0.32,a.april,width=0.08,color='g')
  plt.bar(a.year+0.40,a.may,width=0.08,color='y')
  plt.bar(a.year+0.48,a.june,width=0.08,color='m')
  plt.bar(a.year+0.56,a.july,width=0.08,color='k')
  plt.bar(a.year+0.64,a.aug,width=0.08)
  plt.bar(a.year+0.72,a.sep,width=0.08,color='r')
  plt.bar(a.year+0.8,a.oct,width=0.08,color='b')
  plt.bar(a.year+0.88,a.nov,width=0.08,color='g')
  plt.bar(a.year+0.96,a.dec,width=0.08,color='m')
  fd={'family':'monotype corsiva','color':'k','size':'20','weight':'bold'}
  plt.ylabel('Foreign Arrivals',fontdict=fd,labelpad=5)
  plt.xlabel('years',fontdict=fd,labelpad=5)
  plt.title('Seasonality in foreign arrivals in India',fontdict=fd,pad=20)
  plt.xticks(a.year,labels=['2016','2017','2018'])
  plt.legend(['Jan','Feb','March','April','May','June','July','Aug','Sep','Oct','Nov','Dec'])
  plt.show()



#2:2.2 fta acc to quarter
def fta():
  import pandas as pd, matplotlib.pyplot as plt,numpy as np
  a=pd.read_csv('ssnl_mnth.csv') 
  print(a) 
  x = np.arange(4,1)
  fd={'family':'monotype corsiva','color':'k','size':'20','weight':'bold'}
  plt.bar(a.year,a.qtr1,width=0.15)
  plt.bar(a.year+0.15,a.qtr2,width=0.15)
  plt.bar(a.year+0.3,a.qtr3,width=0.15)
  plt.bar(a.year+0.45,a.qtr4,width=0.15)
  plt.ylabel('visitors',fontdict=fd,labelpad=5)
  plt.xlabel('Years',fontdict=fd,labelpad=5)
  plt.title('Quarter-Wise analysis of arrivals',fontdict=fd,pad=20)
  plt.legend(['Quarter1','Quarter2','Quarter3','Quarter4'])
  plt.show()

#3:3.1 mode of travel
def mode():
  import pandas as pd, matplotlib.pyplot as plt,numpy as np
  a=pd.read_csv('mode_travel.csv') 
  print(a)
  plt.subplot(2,2,1)
  y=np.array([84.5,0.4,14.8])
  l=['air','sea','land']
  plt.pie(y,labels=l,startangle=30,shadow=True,explode=(0.075,0,0),autopct='%1.1f%%')
  plt.legend()
  plt.subplot(2,2,2)
  v=np.array([84.1,0.9,15])
  l=['air','sea','land']
  plt.pie(v,labels=l,startangle=30,shadow=True,explode=(0.075,0,0),autopct='%1.1f%%')
  plt.legend()
  plt.subplot(2,2,3)
  t=np.array([79.6,0.7,19.7])
  l=['air','sea','land']
  plt.pie(t,labels=l,startangle=30,shadow=True,explode=(0.075,0,0),autopct='%1.1f%%')
  plt.legend()
  plt.subplot(2,2,4)
  u=np.array([79.6,0.8,19.6])
  l=['air','sea','land']
  plt.pie(u,labels=l,startangle=30,shadow=True,explode=(0.075,0,0),autopct='%1.1f%%')
  plt.legend()
  plt.title('Mode of travelling',fontdict=fd,pad=20)
  plt.show()

#3:3.2 world and nationality wise distribution
def wndist():
  import pandas as pd, matplotlib.pyplot as plt,numpy as np
  a=pd.read_csv('arrivals.csv') 
  print(a) 
  b=np.arange(100000,1000000,100000)
  l=['South asia','west europe','north america','south east asia',
   'east asia','west asia','east asia','austalasia','central america']
  plt.bar(a.year,a.s_asia,width=0.05,color='b') 
  plt.bar(a.year+0.05,a.w_europe,width=0.05,color='g') 
  plt.bar(a.year+0.1,a.Namerica,width=0.05,color='r') 
  plt.bar(a.year+0.15,a.se_asia,width=0.05,color='c') 
  plt.bar(a.year+0.2,a.e_asia,width=0.05,color='m') 
  plt.bar(a.year+0.25,a.w_asia,width=0.05,color='y') 
  plt.bar(a.year+0.3,a.e_asia,width=0.05,color='k') 
  plt.bar(a.year+0.35,a.australia,width=0.05,color='r') 
  plt.bar(a.year+0.4,a.Camerica,width=0.05,color='y') 
  fd={'family':'monotype corsiva','color':'k','size':'20','weight':'bold'}
  plt.ylabel('Arrivals',fontdict=fd,labelpad=5)
  plt.xlabel('years',fontdict=fd,labelpad=5)
  plt.xticks(a.year,labels=['2016','2017','2018'])
  plt.title('World and nationality wise distribution in India',fontdict=fd,pad=20)
  plt.legend(l)
  plt.show() 
 

#4:4.1 PORTS OF ENTRY
def ports():
  import pandas as pd,matplotlib.pyplot as plt,numpy as np
  a=pd.read_csv('airport.csv')
  print(a)
  plt.bar(a.year,a.arrivals)
  plt.show()
  plt.bar(a.year,a.mum,width=0.1)
  plt.bar(a.year+0.1,a.kol,width=0.1)
  plt.bar(a.year+0.2,a.chennai,width=0.1)
  plt.bar(a.year+0.3,a.bgl,width=0.1)
  plt.bar(a.year+0.4,a.delhi,width=0.1)
  plt.bar(a.year+0.5,a.hyder,width=0.1)
  plt.ylabel('arrivals(in million)',fontdict=fd,labelpad=5)
  plt.xlabel('years',fontdict=fd,labelpad=5)
  plt.title('Ports of Entry in India',fontdict=fd,pad=20)
  plt.xticks(a.year,labels=['2014','2015','2016','2017','2018'])
  plt.legend(['mumbai airport','kolkata airport','chennai airport',
              'bengaluru airport','delhi airport','hyderabad airport'])
  plt.show()
 
#5:5.1 gender
def gender():
  import pandas as pd, matplotlib.pyplot as plt,numpy as np
  a=pd.read_csv('gender.csv')
  print(a)
  plt.bar(a.year,a.male,width=0.2)
  plt.bar(a.year+0.2,a.female,width=0.2)
  plt.bar(a.year+0.4,a.nrep,width=0.2)
  fd={'family':'monotype corsiva','color':'k','size':'20','weight':'bold'}
  plt.ylabel('gender distribution(in %)',fontdict=fd,labelpad=5)
  plt.xlabel('years',fontdict=fd,labelpad=5)
  plt.title('Arrival in India in terms of gender',fontdict=fd,pad=20)
  plt.xticks(a.year,labels=['2014','2015','2016','2017','2018'])
  plt.legend(['Male','Female'])
  plt.show()

#5:5.2 gender distribution
def gendist():
  import pandas as pd,matplotlib.pyplot as plt ,numpy as np
  a=np.array([41.4,57.8,0.8])
  l=['Female','Male','Not Reported']
  plt.pie(a,labels=l,startangle=60,shadow=True,explode=(0,0.05,0),autopct='%1.1f%%')
  plt.title('Arrival in India in terms of gender',fontdict=fd,pad=20)
  plt.legend(l)
  plt.show()

#6:6.1 age group-wise
def agegrp():
  import pandas as pd , matplotlib.pyplot as plt,numpy as np
  a=pd.read_csv('age.csv')
  print(a)
  plt.bar(a.year,a.z_f,width=0.1)
  plt.bar(a.year+0.1,a.f_tf,width=0.1)
  plt.bar(a.year+0.2,a.tf_tf,width=0.1)
  plt.bar(a.year+0.3,a.tf_ff,width=0.1)
  plt.bar(a.year+0.4,a.ff_ff,width=0.1)
  plt.bar(a.year+0.5,a.ff_sf,width=0.1)
  fd={'family':'monotype corsiva','color':'k','size':'20','weight':'bold'}
  plt.ylabel('age-group distribution(in %)',fontdict=fd,labelpad=5)
  plt.xlabel('years',fontdict=fd,labelpad=5)
  plt.title('arrival in India in terms of age-group',fontdict=fd,pad=20)
  plt.xticks(a.year,labels=['2014','2015','2016','2017','2018'])
  plt.legend(['0-14','15-24','25-34','35-44','45-54','55-64'])
  plt.show()

#6:6.2 age pie
def agepie():
  import pandas as pd,matplotlib.pyplot as plt ,numpy as np
  a=np.array([9.3,8.4,18.6,21,19.8,14.2,8.7])
  l=['0-14','15-24','25-34','35-44','45-54','55-64','65 and above']
  plt.pie(a,labels=l,startangle=90,shadow=True,explode=(0,0,0,0.2,0,0,0),autopct='%1.1f%%')
  plt.show()

#7:7.1 purpose of visit
def prps():
  import pandas as pd, matplotlib.pyplot as plt,numpy as np
  a=pd.read_csv('prps_visit.csv')
  print(a)
  plt.bar(a.cntry,a.b_p,width=0.8)
  plt.bar(a.cntry,a.lh_r,width=0.8)
  plt.bar(a.cntry,a.med,width=0.8)
  plt.bar(a.cntry,a.ind_dspr,width=0.8)
  plt.bar(a.cntry,a.others,width=0.8)
  fd={'family':'monotype corsiva','color':'k','size':'20','weight':'bold'}
  plt.ylabel('Arrival (in %)',fontdict=fd,labelpad=5)
  plt.xlabel('years',fontdict=fd,labelpad=5)
  plt.title('arrival in India in terms of purpose of visit',fontdict=fd,pad=20)
  plt.legend(['Business and proffesional','leisure/holiday','medical','indian diaspora','others'])
  plt.xticks(a.cntry,labels=['north america','south america','west europe',
                             'east europe','africa','west asia','south asia',
                             'south east asia','east asia','australia'],rotation=45)

  plt.show()

#8:8.1 foreign exchange currency
def forcur():
  import pandas as pd, matplotlib.pyplot as plt,numpy as np
  a=pd.read_csv('for_exchg.csv')
  print(a)
  l=['2014','2015','2016','2017','2018']
  plt.bar(a.year,a.cr,width=0.25)
  plt.bar(a.year+0.25,a.millions,width=0.25)
  fd={'family':'monotype corsiva','color':'k','size':'20','weight':'bold'}
  plt.ylabel('currency',fontdict=fd,labelpad=5)
  plt.xlabel('years',fontdict=fd,labelpad=5)
  plt.title('foreign exchange currency in India',fontdict=fd,pad=20)
  plt.xticks(a.year,labels=['2014','2015','2016','2017','2018'])
  plt.legend()
  plt.show()
  plt.subplot(2,1,1)
  plt.pie(a.per_chng,labels=l,startangle=130,shadow=True,explode=(0,0,0,0.1,0),autopct='%1.1f%%')
  plt.title('Percentage change(in rupees)')
  plt.subplot(2,1,2)
  plt.pie(a.per_chg,labels=l,startangle=90,shadow=True,explode=(0,0,0,0.1,0),autopct='%1.1f%%')
  plt.title('Percentage change(in dollars)')
  plt.show()

#9:9.1 mode of transport for departures
def trans():
  import pandas as pd, matplotlib.pyplot as plt,numpy as np
  a=np.array([96.47,2.57,0.96])
  l=['Air','Land','Sea']
  plt.pie(a,labels=l,startangle=15,shadow=True,explode=(0.1,0,0),autopct='%1.1f%%')
  plt.show()

#10:10.1 domestic and foreign tourist arrivals
def dfta():
  import pandas as pd, matplotlib.pyplot as plt,numpy as np
  a=pd.read_csv('dom_for.csv')
  print(a)
  plt.bar(a.year,a.domestic,width=0.4)
  plt.bar(a.year+0.4,a.foreign,width=0.4)
  fd={'family':'monotype corsiva','color':'k','size':'20','weight':'bold'}
  plt.ylabel('gender',fontdict=fd,labelpad=5)
  plt.xlabel('years',fontdict=fd,labelpad=5)
  plt.title('domestic and foreign tourist arrivals in India',fontdict=fd,pad=20)
  plt.xticks(a.year,labels=['2014','2015','2016','2017','2018'])
  plt.legend()
  plt.show()

#10:10.2 per-wise domestic and foreign tourist arrivals
def perdfta():
  import pandas as pd, matplotlib.pyplot as plt,numpy as np
  a=pd.read_csv('dom_for.csv')
  print(a)
  plt.bar(a.year,a.an_dom,width=0.4)
  plt.bar(a.year+0.4,a.an_for,width=0.4)
  fd={'family':'monotype corsiva','color':'k','size':'20','weight':'bold'}
  plt.ylabel('type of arrival along with therir annual report',fontdict=fd,labelpad=5)
  plt.xlabel('years',fontdict=fd,labelpad=5)
  plt.title('per-wise domestic and foreign tourist arrivals in India',fontdict=fd,pad=20)
  plt.xticks(a.year,labels=['2014','2015','2016','2017','2018'])
  plt.legend()
  plt.show()

#11:11.1 per-share of top 10 states/UT's in domestic visits
def pershare():
  import pandas as pd,matplotlib.pyplot as plt ,numpy as np
  a=np.array([20.8,15.4,11.6,10.5,6.4,5,4.6,4.5,2.9,2.7])
  l=['Tamil Nadu','Uttar Pradesh','Karnataka','Andhra Pradesh','Maharashtra','Telangana','West Bengal','Madhya Pradesh','Gujarat','Rajasthan']
  plt.pie(a,labels=l,startangle=0,shadow=True,explode=(0.1,0,0,0,0,0,0,0,0,0),autopct='%1.1f%%')
  plt.title('Per-share of top 10 states/UTs in domestic visits',size=18)
  plt.show()

#11:11.2 per-share of top 10 states/UT's in foreign visits
def state():
  import pandas as pd,matplotlib.pyplot as plt ,numpy as np
  a=np.array([21,17.6,13.1,9.5,6.1,5.6,4.2,3.8,3.8,3.2,12.1])
  l=['Tamil Nadu','Maharashtra','Uttar Pradesh','Delhi','Rajasthan','West Bengal','Punjab','Kerala','Bihar','Goa','Others']
  plt.pie(a,labels=l,startangle=90,shadow=True,explode=(0.1,0,0,0,0,0,0,0,0,0,0),autopct='%1.1f%%')
  plt.title('Per-share of top 10 states/UTs in foreign visits',size=18)
  plt.show()

#12 monuments visits domestic as well as foreign
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




