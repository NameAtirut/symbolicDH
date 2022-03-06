import numpy as np
import math as m

def getDHdict(theta, d, alpha, a):
   return {
      'theta': theta,
      'd': d,
      'alpha': alpha,
      'a': a
   }


def getTransformationMatrix(dh_dict):
   theta = dh_dict['theta']
   d = dh_dict['d']
   alpha = dh_dict['alpha']
   a = dh_dict['a']
   
   ## decouple value assignments for readability
   T = np.zeros([4,4])
   
   T[0,0] = m.cos(theta)
   T[0,1] = -m.sin(theta) * m.cos(alpha)
   T[0,2] = m.sin(theta) * m.sin(alpha)
   T[0,3] = a * m.cos(theta)
   
   T[1,0] = m.sin(theta)
   T[1,1] = m.cos(theta) * m.cos(alpha)
   T[1,2] = -m.cos(theta) * m.sin(alpha)
   T[1,3] = a * m.sin(theta)
   
   T[2,0] = 0
   T[2,1] = m.sin(alpha)
   T[2,2] = m.cos(alpha)
   T[2,3] = d
   
   T[3,3] = 1
   return T

def dhTransformAll(theta_list, d_list, alpha_list, a_list):
   matrix_list = []
   T_all = np.identity(4)
   for theta, d, alpha, a in zip(theta_list, d_list, alpha_list, a_list):
      dh = getDHdict(theta=theta,d=d,alpha=alpha,a=a)
      M = getTransformationMatrix(dh)
      matrix_list.append(M)
      T_all = T_all @ M
   return T_all