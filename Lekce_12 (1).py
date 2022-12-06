import matplotlib.pyplot as plt
import pandas

# cvičení 1

kostky = pandas.read_csv("https://kodim.cz/cms/assets/kurzy/python-data-1/python-pro-data-1/vizualizace/excs/excs>hazeni-kostkami/kostky.csv")
#print(kostky)
hody_ = kostky.groupby('hodnota')['hodnota'].count()
#print(hody_)
#kostky.hist(bins = range(2, 14)) # nebo bins = [0.5,1.5,2.5,3.5,4.5,5.5,6.5,7.5,8.5,9.5,10.5,11.5,12.5]
kostky.hist(bins = [1.5,2.5,3.5,4.5,5.5,6.5,7.5,8.5,9.5,10.5,11.5,12.5], color='red', density = True)
plt.title('Hody dvěma kostkami')
plt.xlabel('Hodnoty')
plt.ylabel('Počet hodů')
plt.show()

# cvičení 2

callcentrum = pandas.read_csv("https://kodim.cz/cms/assets/kurzy/python-data-1/python-pro-data-1/vizualizace/excs/excs>call-centrum/callcentrum.csv")
callcentrum = callcentrum["hodnota"].str.split(':', expand=True).astype(int)

callcentrum['cas'] = callcentrum[0] * 60 + callcentrum[1]
#print(callcentrum['cas'])
callcentrum['cas'].hist(width = 150, color = "orange")
plt.show()
callcentrum['cas'].plot(kind = 'box', whis=[0, 99.9])
plt.show()

# cvičení 3

snih = [
  [1968, 480, 351],
  [1969, 462, 663],
  [1970, 443, 490],
  [1971, 518, 444],
  [1972, 537, 420],
  [1973, 446, 941],
  [1974, 446, 691],
  [1975, 450, 477],
  [1976, 356, 395],
  [1977, 381, 652],
  [1978, 345, 525],
  [1979, 430, 762],
  [1980, 266, 316],
  [1981, 533, 781],
  [1982, 471, 769],
  [1983, 407, 801],
  [1984, 526, 633],
  [1985, 391, 488],
  [1986, 361, 624],
  [1987, 470, 471],
  [1988, 506, 514],
  [1989, 333, 208],
  [1990, 462, 909],
  [1991, 438, 443],
  [1992, 364, 488],
  [1993, 452, 579],
  [1994, 484, 519],
  [1995, 460, 809],
  [1996, 465, 682],
  [1997, 431, 814],
  [1998, 463, 595],
  [1999, 460, 512],
  [2000, 503, 750],
  [2001, 462, 951],
  [2002, 429, 413],
  [2003, 405, 738],
  [2004, 477, 777],
  [2005, 385, 316],
  [2006, 368, 417],
  [2007, 513, 635],
  [2008, 448, 689],
  [2009, 525, 443],
  [2010, 427, 225],
  [2011, 460, 618],
  [2012, 417, 742],
  [2013, 517, 247],
  [2014, 466, 552],
  [2015, 523, 441],
  [2016, 422, 690],
  [2017, 420, 699]
]
snihdf = pandas.DataFrame(snih, columns=['rok', 'hora', 'udoli'])
snihdf = snihdf.set_index('rok')

snihdf.plot(kind = 'box')
plt.show()