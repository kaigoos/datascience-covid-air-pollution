import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
import matplotlib.animation as animation

df = pd.read_excel('20200723-02.xlsx', sheet_name = '20200723-02')

x = df["Experimental Time"]
y1 = df["Ipsilateral"]
y2 = df["Contralateral"]

fig = plt.figure(figsize = (14,8))
ax = plt.subplot()
line1, = ax.plot(x, y1, label = 'Ipsilateral')
line2, = ax.plot(x, y2, label = 'Contralateral')

plt.xlabel('Time (min)',fontsize = 20)
plt.ylabel('ICP (mmHg)', fontsize = 20)
plt.title('ICP Monitoring', fontsize = 20)
plt.legend()

plt.axvline(x=0, color = 'black', linestyle='dashed')
plt.axvline(x=18, color = 'black', linestyle='dashed')

def update(num):
    line1.set_data(x[:num], y1[:num])
    line2.set_data(x[:num], y2[:num])

ani = animation.FuncAnimation(fig, update, len(x), interval=1)

# Writer = animation.writers['ffmpeg']
# writer = Writer(fps=15, metadata=dict(artist='Me'), bitrate=1800)
#ani.save('myAnimation.gif', writer='imagemagick', fps=30)

plt.grid()
plt.show()