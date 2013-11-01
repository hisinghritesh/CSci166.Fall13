#!/usr/bin/python

import MySQLdb

# Numpy is a library for handling arrays (like data points)
from dateutil import *
import numpy as np

# Pyplot is a module within the matplotlib library for plotting
import matplotlib.pyplot as plt

DATABASE = "music"
TABLE = "songs"
# DATABASE = "ratest"
# TABLE = "R2"
x_item = 'PK'
y_item = 'High'

def plot(ciris):
   conn = MySQLdb.connect (host = "localhost",
                           user = "cs126",
                           passwd = "cs126",
                           db = DATABASE)
   cursor = conn.cursor ()
   s = "select " +x_item+","+y_item+" from " + TABLE \
                   + " where class like '"+ciris+"%'"
   print s
   cursor.execute (s)
                   
   row = cursor.fetchone ()
   X = []
   Y = []
   while row != None:
      X.append(row[0])
      Y.append(row[1])
      row = cursor.fetchone ()
   cursor.close ()
   conn.close ()
   plt.plot(X,Y,'o')


def test1():
   # Create an array of 100 linearly-spaced points from 0 to 2*pi
   x = np.linspace(0,2*np.pi,100)
   y1 = np.sin(2*x)
   y2 = np.cos(4*x+np.pi/8)/4
   # Create the plot
   plt.plot(x,y1)
   plt.plot(x,y2)
   # Save the figure in a separate file
   plt.savefig('sine_function_plain.png')

   # Draw the plot to the screen
   plt.show()

def test2():
   global x_item, y_item, DATABASE, TABLE
   DATABASE = "cs126a"
   TABLE = "iris_2D"
   x_item = 'x'
   y_item = 'y'
   plot('Iris-setosa')
   plot('Iris-versicolor')
   plot('Iris-virginica')
   plt.show()


