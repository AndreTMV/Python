import matplotlib.pyplot as plt
year = [1950, 1970, 1990, 2010]
pop = [2.519, 3.692, 5.263, 6.972]

year = [1000, 1850, 1900] + year
pop = [1.0, 1.262, 1.650] + pop

plt.plot(year, pop) # grafica con linea

plt.xlabel('Year') 
plt.ylabel('Population')
plt.title('World Population Projections')
plt.yticks([0, 2, 4, 6, 8, 10],
           ['0', '2B', '4B', '6B', '8B', '10B']) # modify intervals

plt.show()
# plt.clf() #clears the plot 

# plt.scatter(year, pop) # grafica con puntos solo
# plt.show()
# plt.clf()

#examples
# Specify c and alpha inside plt.scatter()
# plt.scatter(x = gdp_cap, y = life_exp, s = np.array(pop) * 2, c = col, alpha=0.8)

# # Previous customizations
# plt.xscale('log') 
# plt.xlabel('GDP per Capita [in USD]')
# plt.ylabel('Life Expectancy [in years]')
# plt.title('World Development in 2007')
# plt.xticks([1000,10000,100000], ['1k','10k','100k'])

# Additional customizations
# plt.text(1550, 71, 'India')
# plt.text(5700, 80, 'China')

# # Add grid() call
# plt.grid(True)

# Show the plot
plt.show()
# # Show the plot
# plt.show()
