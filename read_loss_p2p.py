import os 
import matplotlib.pyplot as plt 



# 打开文件并使用readlines读取所有行
with open('/home/user9/USenhance2023/checkpoints/pix2pix_ultrasound_2000/loss_log.txt', 'r', encoding='utf-8') as file:
    lines = file.readlines()

# 打印文件内容
G_GAN = []
G_L1 = []
D_real = []
D_fake = []

epoch = []
all_loss = []
last_epoch = 1
for line in lines[1:]:
    cur_epoch = int(line.split("epoch: ")[1].split(",")[0])
    if cur_epoch != last_epoch:
        
        last_epoch = cur_epoch
        tmp = 0
        G_GAN.append(float(gg))
        G_L1.append(float(gl))
        D_real.append(float(dr))
        D_fake.append(float(df))
        
        
        tmp += float(gg)
        tmp += float(gl)
        tmp += float(dr)
        tmp += float(df)
        
        all_loss.append(tmp)
    gg = line.split("G_GAN: ")[1].split(" ")[0]
    gl = line.split("G_L1: ")[1].split(" ")[0]
    dr = line.split("D_real: ")[1].split(" ")[0]
    df = line.split("D_fake: ")[1].split(" ")[0]
    
        


plt.plot(G_GAN)
plt.xlabel("epoches")
plt.ylabel("G_GAN loss")
plt.savefig("/home/user9/USenhance2023/p2p_loss/GGAN.jpg")
plt.cla()
plt.plot(G_L1)
plt.xlabel("epoches")
plt.ylabel("G_L1 loss")
plt.savefig("/home/user9/USenhance2023/p2p_loss/GL.jpg")
plt.cla()
plt.plot(D_real)
plt.xlabel("epoches")
plt.ylabel("D_real loss")
plt.savefig("/home/user9/USenhance2023/p2p_loss/DR.jpg")
plt.cla()
plt.plot(D_fake)
plt.xlabel("epoches")
plt.ylabel("D_fake loss")
plt.savefig("/home/user9/USenhance2023/p2p_loss/df.jpg")
plt.cla()
plt.plot(all_loss)
plt.xlabel("epoches")
plt.ylabel("all loss")
plt.savefig("/home/user9/USenhance2023/p2p_loss/all.jpg")
plt.cla()
        