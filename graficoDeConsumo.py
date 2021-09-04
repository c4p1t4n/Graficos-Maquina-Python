import matplotlib.pyplot as plt
import matplotlib.animation as animation
import psutil
from matplotlib.pylab import *



fig=figure(num = 0, figsize = (12, 8))#, dpi = 100)
fig.suptitle("Dados de Máquinas de recarga")
ax=subplot2grid((2, 2), (1, 0), colspan=2, rowspan=1)
ax2=subplot2grid((2, 2), (0, 1))
ax3= subplot2grid((2, 2), (0, 0))
xsCpu, ysCpu,ys2Cpu,ys3Cpu =[0],[0],[0],[0]
xsRam, ysRam,ys2Ram,ys3Ram =[0],[0],[0],[0]
xsDisco,ysDisco,ysDisco2,ysDisco3 = [0],[0],[0],[0]

time= 0
def updateGraphCpu(interval, xs, ys,ys2,ys3):

    global time
    time = time + 1
    # ------------------------------------CPU-------------------------------------------
    cpu =psutil.cpu_percent()
    cpu2 = round((cpu * 1.1),2)
    cpu3= round(cpu2+ (cpu2*0.05))    
    xsCpu.append(time)
    ysCpu.append(cpu)
    ys2Cpu.append(cpu2)
    ys3Cpu.append(cpu3)     
    ax.clear()
    ax.plot(xsCpu, ysCpu,label="Cpu 01",color="black")
    ax.plot(xsCpu,ys2Cpu,label="Cpu 02",color="purple")
    ax.plot(xsCpu,ys3Cpu,label="Cpu 03",color="red")
    ax.set_label('Consumo de CPU')
    ax.fill_between(xsCpu,ysCpu,color ="#AED5FC")     
    ax.set_ylabel('Consumo de CPU')
    ax.set_xlabel('Tempo')
    ax.set_title("Consumo de CPU / Tempo")
    ax.legend()
    ax.grid(True)
     # ------------------------------------Memoria-------------------------------------------
    memory =psutil.virtual_memory().percent
    memory2=round((memory * 1.15),2)
    memory3= round(memory2 - (memory2*0.05),2)
    
    xsRam.append(time)
    ysRam.append(memory)
    ys2Ram.append(memory2)
    ys3Ram.append(memory3)     
      
    ax2.clear()
    ax2.plot(xsRam,ysRam,label="Memoria 01",color="black")
    ax2.plot(xsRam,ys2Ram,label="Memoria 02",color="purple")
    ax2.plot(xsRam,ys3Ram,label="Memoria 03",color="red")
    ax2.set_ylabel('Consumo de RAM')
    ax2.set_xlabel('Tempo')
    ax2.set_title("Consumo de Ram / Tempo")
    ax2.legend()
    ax2.grid(True)
    # ------------------------------------Disco-------------------------------------------
    try:
        disco=psutil.disk_usage("/").percent
           
    except:
        disco=psutil.disk_usage("c:/").percent
       
    disco2 = disco - (disco * 0.05) 
    disco3 = disco2  +5
    xsDisco.append(time)
    if (disco < 100 and  disco2 <100 and disco3 < 100):        
        ysDisco.append(disco)
        ysDisco2.append(disco2)
        ysDisco3.append(disco3)
    else:
        ysDisco.append(disco)
        ysDisco2.append(disco2)
        ysDisco3.append(disco3)
        
      
    ax3.clear()
    ax3.plot(xsDisco,ysDisco,label="Disco 01",color="black")
    ax3.plot(xsDisco,ysDisco2,label="Disco 02",color="purple")
    ax3.plot(xsDisco,ysDisco3,label="Disco 03",color="red")
    ax3.set_ylabel('Consumo de Disco')
    ax3.set_xlabel('Tempo')
    ax3.set_title("Consumo de Disco / Tempo")
    plt.legend()
    ax3.grid(True)
    if(time % 30 == 0):
        fig.savefig(f'Dados Maquinas de Cartão { time/10 }.png')
        
    ax.set_ylim(0,100)
    ax2.set_ylim(0,100)
    ax3.set_ylim(0,100)
    
        


        
    
        
    




graph = animation.FuncAnimation(fig,updateGraphCpu, fargs=(xsCpu, ysCpu,ys2Cpu,ys3Cpu)
, interval=1000)

plt.show()


